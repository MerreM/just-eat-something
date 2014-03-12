import requests
from bs4 import BeautifulSoup
import random
import urllib
from pprint import pprint

POST_CODE_QUERY = "http://www.just-eat.co.uk/Postcode/Cuisines?"

GET_RESTARUNTS = "http://www.just-eat.co.uk/area/nr1-norwich/"



def filter_styles(styles):
    ## Filter based on choices
    ## Filter based on rating
    return styles

def get_available_styles(location):
    ## Get all options
    ## Remove all those that all closed
    response = requests.get(POST_CODE_QUERY+urllib.urlencode(location))
    styles = dict(response.json())
    styles = styles["cuisines"]
    styles_dict = {}
    for style in styles:
        styles_dict[style["Name"]]=style["FriendlyName"]
    pprint(styles_dict)
    return filter_styles(styles)

def get_styles_for_location(location):
    return get_available_styles(location)

def get_restaurants_by_style(style):
    restaurants = None
    return restaurants

def get_delivery_fee(restaurant):
    pass

def get_restaurant(style):
    choices = get_restaurants_by_style(style)
    choice = random.choice(choices)
    delivery_fee = get_delivery_fee(choice)
    return choice

def get_catergories(menu):
    ## Get Starters/Beverages/Desserts
    ## Errything else is Mains.
    ## Each main must have Spice/Veg/Vegan Attrs.
    pass

def get_menu(restaurant):
    menu = None
    catergories = get_catergories(menu)
    return menu

def main():
    postcode = raw_input("Post code>>>\n")
    location = {
        "postcode":postcode,
    }
    styles = get_styles_for_location(location)
    style = random.choice(styles)
    restaurant = get_restaurant(style)
    menu = get_menu(restaurant)

if __name__ == "__main__":
    main()
