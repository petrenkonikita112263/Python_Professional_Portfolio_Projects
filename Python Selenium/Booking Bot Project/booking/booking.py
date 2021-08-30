import os

from selenium import webdriver
from . import constants as const


class Booking():

    def __init__(self, driver_path=const.DRIVER_PATH):
        """Constructor of the class"""
        self.browser = webdriver.Edge(driver_path)

    def get_home_page(self):
        """Load the url web page"""
        self.browser.get(const.HTML_URL)
