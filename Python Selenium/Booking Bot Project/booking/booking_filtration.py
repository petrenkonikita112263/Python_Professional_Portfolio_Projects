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
