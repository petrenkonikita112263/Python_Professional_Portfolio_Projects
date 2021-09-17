from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    """Class with method that will parse the hotel list from html page."""

    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        """Return the list of hotels from main box in result (1st) page."""
        return self.boxes_section_element.find_elements_by_class_name(
            "sr_property_block"
        )

    def pull_titles(self):
        """From deal_boxes list grab each title of hotels."""
        for deal_box in self.deal_boxes:
            hotel_title = deal_box.find_element_by_class_name(
                "sr-hotel__name"
            ).get_attribute("innerHTML").strip()
            print(hotel_title)

    def pull_deal_box_attributes(self):
        """From deal_boxes grab hotel title, its price, rating(score) and save it to the list."""
        pass
