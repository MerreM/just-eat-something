import requests
from bs4 import BeautifulSoup
import random

def filter_styles(styles):
    ## Filter based on choices
    ## Filter based on rating
    return styles

def get_available_styles(location):
    ## Get all options
    ## Remove all those that all closed
    styles = None
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

def get_menu(restaurant):
    menu = None
    catergories = get_catergories(menu)



def main():
    location = raw_input("Post code")
    styles = get_styles_for_location(location)
    style = random.choice(styles)
    restaurant = get_restaurant(style)



