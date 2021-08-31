from booking.booking import Booking

if __name__ == "__main__":
    booking_instance = Booking()
    booking_instance.get_home_page()
    # this line can be run once, to change the currency value, by sending the currency type to it
    # booking_instance.change_currency()
    booking_instance.fill_place_name("Київ")