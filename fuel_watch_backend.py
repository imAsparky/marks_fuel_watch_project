# import glob
# import json
# import os
# from datetime import datetime, timedelta

import feedparser
# import fuel_watch_filters as filters
# import pytz
import requests
# import safer

import pprint as pp

# Constants to keep track of the fuel watch data file list
DATA_FILE_PATH = "fuel_data"
DATA_FILE_LIST = ""


# ========URL FUNCTIONS===========


def get_fuel_watch_data(filters={},*args, **kwargs):
    """Constructs a URL with selections on which data to
    collect from the Fuel Watch RSS Feed

    PARAMATERS
    ==========

    """

    # The URL to collect all the Fuel Watch data available without filters
    BASE_URL = "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?"


    if filters:

        data = requests.get(BASE_URL, params=filters)

        print("&&&&&&&&&&&&&&&&&& URL\n", data.url)

            # If response is ok, 200 parse the data
        if data.status_code == 200:
                parsed_data = feedparser.parse(data.content)["entries"]

        return parsed_data

    else:

        data = requests.get(BASE_URL)

            # If response is ok, 200 parse the data
        if data.status_code == 200:
                parsed_data = feedparser.parse(data.content)["entries"]

        return parsed_data




if __name__ == "__main__":

    # print("URL ", get_fuel_watch_url(filters={}))

    print("***************************************\nGet Data\n")


    pp.pprint(get_fuel_watch_data(filters={"Product": 1, "Suburb":"6064",'Brand': 5,})[0])


