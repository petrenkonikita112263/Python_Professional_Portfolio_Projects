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

    def fill_place_name(self, place_to_go):
        """Sending the place name to the input field."""
        input_place_field = self.browser.find_element_by_id("ss")
        input_place_field.clear()
        input_place_field.send_keys(place_to_go)
        first_result = self.browser.find_element_by_css_selector(
            "li[data-i='0']"
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        """Select the two days from calendars."""
        check_in_element = self.browser.find_element_by_css_selector(
            f"td[data-date='{check_in_date}']"
        )
        check_in_element.click()
        check_out_element = self.browser.find_element_by_css_selector(
            f"td[data-date='{check_out_date}']"
        )
        check_out_element.click()

    def select_adult_human(self, quantity=1):
        """Select the adult number in the field."""
        selection_element = self.browser.find_element_by_id("xp__guests__toggle")
        selection_element.click()

        # set the adult number to 1
        while True:
            default_adult_number = self.browser.find_element_by_css_selector(
                "button[aria-label='Дорослі: зменшити кількість']"
            )
            default_adult_number.click()
            adult_number_element = self.browser.find_element_by_id("group_adults")
            adult_number = adult_number_element.get_attribute("value")
            if int(adult_number) == 1:
                break
        add_adult_element = self.browser.find_element_by_css_selector(
            "button[aria-label='Дорослі: збільшити кількість']"
        )

        # increase the adult number to the input number
        for _ in range(quantity - 1):
            add_adult_element.click()
