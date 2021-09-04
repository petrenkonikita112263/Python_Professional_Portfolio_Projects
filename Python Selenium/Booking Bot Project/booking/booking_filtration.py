from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    """Class that filter information by hotel stars and prices."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def apply_star_rating(self, star_value=3):
        """Filtration by ratings in start, by default chooses the 3 stars."""
        star_box = self.driver.find_element_by_id("filter_class")
        star_child_element = star_box.find_elements_by_css_selector(
            "*"
        )
        for star_element in star_child_element:
            if str(star_element.get_attribute("innerHTML")).strip() == f"{star_value} зірки":
                star_element.click()


    def sort_by_most_user_ratings(self):
        """Use another filter to filter by stars (rating)."""
        high_ratings = self.driver.find_element_by_css_selector(
            "li[data-id='class']"
        )
        high_ratings.click()

    def apply_walking(self):
        """Filtration by foot walking at downtime."""
        activities_option = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/div[6]/form/fieldset/div[1]/div/div[13]/div[2]"
        )
        foot_walking = activities_option.find_element_by_css_selector(
            "a[data-id='popular_activities-70']"
        )
        foot_walking.click()
