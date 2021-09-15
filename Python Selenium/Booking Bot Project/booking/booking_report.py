class BookingReport:
    """Class with method that will parse the hotel list from html page."""

    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        """Return the list of hotels from main box in result (1st) page."""
        return self.boxes_section_element.find_elements_by_class_name(
            "sr_property_block"
        )
