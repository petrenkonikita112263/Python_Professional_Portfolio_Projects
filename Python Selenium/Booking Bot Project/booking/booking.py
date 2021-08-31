import os

from selenium import webdriver
from . import constants as const


class Booking():

    def __init__(self, driver_path=const.DRIVER_PATH):
        """Constructor of the class"""
        self.browser = webdriver.Edge(driver_path)
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()

    def get_home_page(self):
        """Load the url web page"""
        self.browser.get(const.HTML_URL)

    def change_currency(self, currency="UAH"):
        """Change the type of currency on the page.
        By default in my country it's UAH."""
        currency_element = self.browser.find_element_by_css_selector(
            "button[data-tooltip-text='Виберіть валюту']"
        )
        currency_element.click()
        selected_currency_element = self.browser.find_element_by_css_selector(
            f"a[data-modal-header-async-url-param*='selected_currency={currency}']"
        )
        selected_currency_element.click()
