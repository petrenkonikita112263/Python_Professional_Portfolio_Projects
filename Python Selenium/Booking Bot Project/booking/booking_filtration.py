from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    """Class that filter information by hotel stars and prices."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
