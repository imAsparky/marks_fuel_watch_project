from datetime import datetime

import fuel_watch_backend as fwb
import fuel_watch_filters as filters


def html_head():
    """Returns a webpage head.
    """
    head = """
    <!DOCTYPE html>
<html>
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-172466972-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-172466972-1');
    </script>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="icon" type="image/png" href="static/media/favicon-16x16.png" />
    <link rel="stylesheet" href="static/main.css">
    <title>
        Marks Fuel Watch Project
    </title>

</head>
    """
    return head


def html_home_navbar():
    """Returns a webpage navbar.
    """
    navbar = """
        <div>
            <nav>
                <span style="float:right;">
                <img class="pull-right" src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?
                 pfdrid_c=true" alt="../static/media/fuel_watch_logo.PNG"
                 height="75" width="105">
                </span>
                <span>
                <h3 class="logo">Marks Fuel Watch Project</h3>
                <p class="left"> Form Last Update Time:
        """

    navbar = navbar + fwb.get_perth_date_time_as_string(day="today", time=True)

    navbar = (
        navbar
        + """
            </p>
                <a href="/about" color:"#27AE60">About Project</a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
            </nav>
        </div>
    """
    )

    return navbar


def html_about_navbar():
    """Returns a webpage navbar.
    """
    navbar = """
        <div>
            <nav>
                <span style="float:right;">
                <img class="pull-right" src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?
                 pfdrid_c=true" alt="../static/media/fuel_watch_logo.PNG"
                 height="75" width="105">
                </span>
                <h3 class="logo">Marks Fuel Watch Project</h3>
                <a href="/" color:"#27AE60">Home</a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
            </nav>
        </div>
    """
    return navbar


def html_home_body(filtered=True, **kwargs):
    """Return a HTML string containing the fuel watch data table.
    """

    product = filters.Product()
    suburb = filters.Suburb()
    data = fwb.get_fuel_data(filtered, **kwargs)

    today = fwb.get_perth_date_time_as_string(day="today")

    body = """
<hr>
<div style="overflow-x:auto;">
<table border="1" width="100%">
<thead>
<tr>
    """

    select_form = """
    <div>
    <form>
      <label for="product">Product:</label>
      <select name="product" id="product">
    """
    # Create the Product dropdown selector
    for key in product.keys():
        if key == "FilterName":
            key = ""
        # Renders the returned selectors with selection made by user
        if key != kwargs["Product"]:
            select_form = select_form + f"<option value={key}>{key}</option>"
        else:
            select_form = select_form + f"<option value=\"{key}\" selected>{key}</option>"

    select_form = (
        select_form
        + """
      </select>
      &nbsp;
      <label for="suburb">Suburb:</label>
      <select name="suburb" id="suburb">
    """
    )
    for key in suburb.keys():
        if key == "FilterName":
            key = ""
        # Renders the returned selectors with selection made by user
        if key != kwargs["Suburb"]:
            select_form = select_form + f"<option value={key}>{key}</option>"
        else:
            select_form = select_form + f"<option value={key} selected>{key}</option>"

    select_form = (
        select_form
        + """
      </select>
      &nbsp;
      &nbsp;
      <label for="surrounding">Include Surrounding:</label>
      """
    )
    if kwargs["Surrounding"] == "yes":
        select_form = (
            select_form
            + """
        <input type="radio" checked="True" id="yes" name="surrounding" value="yes" />
        <label for="yes">Yes</label>
        <input type="radio" id="no" name="surrounding" value="no" />
        <label for="no">No</label>
        """
        )
    else:
        select_form = (
            select_form
            + """
        <input type="radio" id="yes" name="surrounding" value="yes" />
        <label for="yes">Yes</label>
        <input type="radio" checked="True" id="no" name="surrounding" value="no" />
        <label for="no">No</label>
        """
        )
    select_form = (
        select_form
        + """
      &nbsp;
      &nbsp;
      <input class="select" type="submit" value="submit" />
      &nbsp;
      &nbsp;
      <label class='tomorrow'>Tomorrows data included after 2:30 PM</label>
    </form>
    <br>
    <hr>
    </div>
    """
    )

    body = body + select_form

    try:
        # Create the column labels from the data keys
        for key in data[0].keys():
            body = body + "<th>" + key.capitalize() + "</th>"
        # Close out the column headings
        body = body + "\n</tr>\n</thead>\n</div>"

        # Add each row of data to the table
        body = body + "\n<tbody>"
        for x in data:
            if x["updated"] == today:

                body = body + "\n<tr class='today'>"

            else:
                body = body + "\n<tr class='tomorrow'>"

            for key, value in x.items():

                body = body + "<td>" + str(value) + "</td>"

            body = body + "\n</tr>"
        body = body + "\n</tbody>"

        return body

    except Exception:
        body = (
            body
            + """
        <div>
            <p class='error'>The search you have requested doesnt seem to have the information available</p>
            <p class='error'>Please make another selection, perhaps with a nearby town or include surroundings may help</p>
            &nbsp;
            <img class='imgcenter' src="static/media/oops.png" alt="OOPS! An Error Has Occured" style="width:500px;height:300px;">
        </div>
        """
        )

        return body


def html_about_body():
    """ Return a HTML string containing the About page body
    """

    about = """
    <body style="overflow-x:auto;">
        <h2>About the Fuel Watch Project</h2>
        <hr>
        <br>
        <div>
            <p class='l'>
                This project is a result of a Learn Python Course developed by
                Robin Chew.
            </p>
            <p class='l'>
               The course was run for 10 Weeks from march 2020 at the Bentley
               Technology centre in Perth Western Australia, there was several
               break due to the covid 19 pandemic.
            </p>
            <p class='l'>
               The objective of the course was to get the Perth Fuel Watch RSS
               feed, extract the data into a format that suited our
               own needs, then present the data in a html page using Flask.
            </p>
        </div>

    </body>
            """
    return about


def html_footer():

    footer = """
        <div class="footer">
            <hr>
            <strong>
            <em>

            All data is sourced from the Fuel Watch Website,
            produced by the Government of Western Australia.

            </em>
            </strong>
            <hr>
        </div>


    """
    return footer


def generate_home_html_string(filtered=True, **kwargs):
    """

    """

    # Put the suburb name into the correct format
    kwargs["Suburb"] = str.capitalize(kwargs["Suburb"])

    return (
        html_head()
        + html_home_navbar()
        + html_home_body(filtered, **kwargs)
        + html_footer()
    )


def generate_about_html_string():
    """
    """
    return html_head() + html_about_navbar() + html_about_body() + html_footer()


# + html_style()


if __name__ == "__main__":
    """Run the fuel watch html generator with default filters

    """
    print("Generating file")
    kwargs = {
        "Region": "",
        "Suburb": "",
        "Product": "",
        "Day": "",
        "Surrounding": "",
        "Brand": "",
        "Sort_on": "price",
        "keys_of_interest": [
            "updated",
            "price",
            "trading-name",
            "brand",
            "address",
            "location",
        ],
    }

    generate_home_html_string(filtered=True, **kwargs)
    print("Fuel Watch.html has been generated and can be found in \html_files")
