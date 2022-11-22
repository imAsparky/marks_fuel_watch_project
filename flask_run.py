# import fuel_watch_filters as filters
from flask import Flask, request
# from fuel_watch_backend import get_tomorrows_RSS_fuel_data
# from fuel_watch_frontend import generate_about_html_string, generate_home_html_string

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask! again"
# def fuel_watch():
#     # product = request.args.get("product", '')

#     kwargs = {
#         "StateRegion": "",
#         "Region": "",
#         "Suburb": request.args.get("suburb", ""),
#         "Product": request.args.get("product", ""),
#         "Day": "",
#         "Surrounding": request.args.get("surrounding", ""),
#         "Brand": "",
#         "Sort_on": "price",
#         "keys_of_interest": [
#             "updated",
#             "price",
#             "trading-name",
#             "brand",
#             "address",
#             "location",
#         ],
#     }
#     # get_tomorrows_RSS_fuel_data(filter=True, **kwargs)

#     return generate_home_html_string(filtered=True, **kwargs)


# @app.route("/about")
# def about():
#     return generate_about_html_string()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1)
