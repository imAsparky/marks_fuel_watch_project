import glob
import json
import os
from datetime import datetime, timedelta

import feedparser
import fuel_watch_filters as filters
import pytz
import requests
import safer

# Constants to keep track of the fuel watch data file list
DATA_FILE_PATH = "fuel_data"
DATA_FILE_LIST = ""


# ========SORT FUNCTIONS===========


def by_brand(item):
    return item["brand"]


def by_location(item):
    return item["location"]


def by_price(item):
    return item["price"]


# ========URL FUNCTIONS===========


def construct_fuel_watch_url(**kwargs):
    """Constructs a URL with selections on which data to
    collect from the Fuel Watch RSS Feed

    PARAMATERS
    ==========

    param:: brand:- String, a number supplies the Brand ID,
                            default is all brands
    param:: day:- String, default today, options tomorrow, yesterday
    param:: product:-  String, a number supplies the product ID
                            default is all products
    param:: region:- String, a number supplies the region ID
    param:: suburb:- String, supplies the suburb name

    param:: surrounding:- String, default yes , includes surrounding suburbs

    """

    # The URL to collect all the Fuel Watch data available without filters
    URL = "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?"

    # Get the valid filters and put them in a dict for ease of checking
    VALID_URL_FILTERS = {
        "Brand": filters.Brand(),
        "Day": filters.Day(),
        "Product": filters.Product(),
        "Region": filters.Region(),
        "StateRegion": filters.StateRegion(),
        "Suburb": filters.Suburb(),
        "Surrounding": filters.Surrounding(),
    }

    # Construct a URL to get the required data
    for key, value in kwargs.items():

        # Check the filters supplied are valid
        if valid_fuel_watch_filter(key, value):

            # Check the length of URL string, if >54 then an "&"
            # needs to be concatinated with the additional filter
            if value:
                if len(URL) < 55:
                    URL = URL + "".join(
                        join_string_with_operator([key, VALID_URL_FILTERS[key][value]])
                    )
                else:
                    URL = (
                        URL
                        + "&"
                        + "".join(
                            join_string_with_operator(
                                [key, VALID_URL_FILTERS[key][value]]
                            )
                        )
                    )
    print(URL)
    return URL


def join_string_with_operator(values=[], operator="="):
    """Joins 2 strings with an operator and returns the new string

    PARAMATERS
    ==========

    param:: values: List of strings
    param:: operator: String, this is the operater to join the string
                        default is '='
    """
    return str(operator).join(values)


def get_dict_key_from_value(value, **kwargs):
    """Return the dictionary key based on a value
    """
    for key, val in kwargs.items():
        if val == value:
            return key


def valid_fuel_watch_filter(key, value):
    """Validate the filter selections before getting the fuel watch data"""

    VALID_URL_FILTERS = {
        "Brand": filters.Brand(),
        "Day": filters.Day(),
        "Product": filters.Product(),
        "Region": filters.Region(),
        "StateRegion": filters.StateRegion(),
        "Suburb": filters.Suburb(),
        "Surrounding": filters.Surrounding(),
    }

    if key in VALID_URL_FILTERS.keys() and value in VALID_URL_FILTERS[key]:
        return True

    # ALert user some how.... print for now
    elif key in VALID_URL_FILTERS.keys() and value != "":
        print(
            "Please supply a valid filter,\
             this is not valid\n",
            key,
            " : ",
            value,
            "\n default values have been used",
        )

        return False

    else:
        return False


# ========FILE HANDLING===========


def get_tomorrows_RSS_fuel_data(filter=True, **kwargs):
    """Get tomorrows Fuel Watch Data and save to file
    """
    file_failed_list = []
    days = ["tomorrow"]

    kwargs["Day"] = "tomorrow"

    # Get the dict of products to iterate over
    prod = filters.Product()

    # Cycle through the available days and collect fuel watch data
    if tomorrow_RSS_data_available():
        for day in days:
            kwargs["Day"] = day

            for key in prod.keys():

                # FilterName is not a Product
                if key != "FilterName":
                    kwargs["Product"] = key
                    # Construct URL to get fuel watch data
                    url = construct_fuel_watch_url(**kwargs)

                    # Get tomorrows fuel watch data
                    get_data = requests.get(url)

                    # If response is ok, 200 parse the data
                    if get_data.status_code == 200:
                        parsed_data = feedparser.parse(get_data.content)["entries"]

                        # Make a file name with the the parsed data parameters
                        # for saving to disk.
                        file_name = (
                            join_string_with_operator(
                                values=[
                                    parsed_data[0]["updated"],
                                    kwargs["StateRegion"],
                                    kwargs["Product"],
                                ],
                                operator="_",
                            )
                            + ".json"
                        )

                        # Use safer to  save to disk to ensure files are
                        # not corrupted before closing.
                        with safer.open(
                            os.path.join("fuel_data", file_name), "w"
                        ) as fp:
                            json.dump(
                                parsed_data, fp
                            )  # All of the file is written, or none

                        if not check_file_name_saved_on_disk(file_name):
                            file_failed_list.append(file_name)

    print("Files Failed ", file_failed_list)


def check_file_name_saved_on_disk(file_name):
    """ Confirm file was written to disc

    PARAMATERS
    ==========

    param:: file_name
    """

    return file_name in get_saved_filename_list()


def get_saved_filename_list(file_path=""):
    """ Returns the file names currently saved on disk

    PARAMATERS
    ==========

    param:: file_path: str default is DATA_FILE_PATH
    """

    if not file_path:

        return list(sorted(glob.glob(DATA_FILE_PATH + "/*")))

    else:
        return list(sorted(glob.glob(file_path + "/*")))


# ========DATE/TIME HANDLING===========


def get_day_date(day="tomorrow"):
    """Return the date for the supplied day for Perth TZ

    Paramaters
    ==========
    param:: day: str options today, tomorrow, yesterday

    """
    timeZ_Pe = pytz.timezone("Australia/Perth")
    today = datetime.date.today(timeZ_Pe)
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)

    if day == "today":
        return today

    elif day == "tomorrow":
        return tomorrow

    else:
        return yesterday


def get_perth_date_time_as_string(day="today", date=True, time=False):
    """Returns TZ aware date time for Perth Western Australia
    """
    date_format = "%Y-%m-%d"
    time_format = "%H:%M:%S"

    timeZ_Pe = pytz.timezone("Australia/Perth")

    # Generate the correct format for the return date time request
    if date and not time:
        return_format = date_format
    elif date and time:
        return_format = " ".join([date_format, time_format])
    else:
        return_format = time_format

    # Generate today
    # Answer 18 from
    today = timeZ_Pe.fromutc(datetime.utcnow())

    if day == "today":
        return today.strftime(return_format)

    elif day == "tomorrow":
        return (today + timedelta(days=1)).strftime(date_format)

    else:
        return (today - timedelta(days=1)).strftime(date_format)


def tomorrow_RSS_data_available():
    """ Tomorrows Fuel Watch data is available after 14:30 today
    """
    timeZ_Pe = pytz.timezone("Australia/Perth")
    # now = datetime.now(timeZ_Pe)
    now = timeZ_Pe.fromutc(datetime.utcnow())
    data_available_now = now.replace(hour=14, minute=30, second=0, microsecond=0)

    return now > data_available_now


def fuel_watch_filtered_on_keys(data=[], keys_of_interest=[]):
    """Returns a list of dictionaries filtered on keys_of_interest


    Parameters
    ==========

    param:: data:- a list of dictionaries
    param:: keys_of_interest: a list of keys to extract and return

    """

    # Default set of keys from fuel watch data we want to
    # display on our website

    if not keys_of_interest:

        # Create default keys of interest, using the  html page column order
        keys_of_interest = [
            "updated",
            "price",
            "trading-name",
            "brand",
            "address",
            "location",
        ]

    # Create an empty list to store dicts filtered on keys of interest
    filtered_list = []

    # Filter the data using keys_of_interest
    for x in data:
        data_filtered = dict()

        for key in keys_of_interest:
            data_filtered[key] = x[key]

        filtered_list.append(data_filtered)

    return filtered_list


# TODO Move all kwarg filter validations to entry point get_fuel_data
def get_fuel_data(filtered=True, **kwargs):
    """Returns the requested fuel watch information

    Paramaters
    ==========

    Paramaters are essentially just filters to limit the size of the data being
    requested from the fuel watch website.

    param:: *filtered:-* Boolean. Default=True
                         False: Data is not filtered on the
                            supplied options below

    **kwargs:FILTERS**

    param:: *Region:-* Integer as a String, supplies the region ID
    param:: *Suburb:-* String supplies the suburb name
    param:: *Product:-*  Integer as a String, supplies the product ID
    param:: *Day:-* String, default today_tomorrow, options tomorrow,
                            yesterday, today
    param:: *Surrounding:-* String, default yes , includes surrounding suburbs
    param:: *Brand:-* An integer supplied as a string for the product ID,
                             default is all products


    **kwargs: DATA: Presentation options

    param:: *Sort_on:-* A list of keys to sort the data, default sort on price
    param:: *keys_of_interest:-* A list of keys to filter fuel watch data,
                                    a filtered data set using
                                    default keys_of_interest will be returned
                                    if no list is supplied

    """

    # Read RSS data and extract just data["entries"] into a list
    # The RSS Feed is a dictionary of mixed data structures,
    # we are only interested in the "entries" which contain all the
    # fuel watch info.

    # Check if today and tomorrows fuel watch info is required

    if kwargs["Day"] == "" or kwargs["Day"] == "today_tomorrow":

        # Construct URL to get todays fuel watch data
        kwargs["Day"] = "today"
        url_today = construct_fuel_watch_url(**kwargs)

        # Get todays fuel watch data
        data = feedparser.parse(requests.get(url_today).content)["entries"]

        if tomorrow_RSS_data_available():
            # Construct URL to get tomorrows fuel watch data
            kwargs["Day"] = "tomorrow"
            url_tomorrow = construct_fuel_watch_url(**kwargs)

            # Get tomorrows info and data.extend() to todays info
            data.extend(feedparser.parse(requests.get(url_tomorrow).content)["entries"])

    else:
        url = construct_fuel_watch_url(**kwargs)
        data = feedparser.parse(requests.get(url).content)["entries"]

    if filtered:
        filtered_data = fuel_watch_filtered_on_keys(
            data=data, keys_of_interest=kwargs["keys_of_interest"]
        )

        if kwargs["Sort_on"]:

            if kwargs["Sort_on"] == "brand":

                return sorted(filtered_data, key=by_brand)

            elif kwargs["Sort_on"] == "location":
                return sorted(filtered_data, key=by_location)

            elif kwargs["Sort_on"] == "price":
                return sorted(filtered_data, key=by_price)

        else:
            return sorted(filtered_data, key=by_price)

    else:
        sorted_data = sorted(data, key=by_price)

        return sorted_data
