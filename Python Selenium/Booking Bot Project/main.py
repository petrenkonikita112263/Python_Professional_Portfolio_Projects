from booking.booking import Booking


def main():
    booking_instance = Booking()
    booking_instance.get_home_page()
    # this line can be run once, to change the currency value, by sending the currency type to it
    # booking_instance.change_currency()
    booking_instance.fill_place_name(input("Куди їдемо? "))
    booking_instance.select_dates(input("Дата приїзду (наприклад 2021-01-01) "),
                                  input("Дата виїзду (наприклад 2021-01-01 "))
    booking_instance.select_adult_human(int(input("Кількість осіб ")))
    booking_instance.search_info()
    # booking_instance.apply_filtrations()
    booking_instance.report_result()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if "in PATH" in str(e):
            print(
                "You are trying to run the bot from command line \n"
                "Please add to PATH your Selenium Drivers \n"
                "Windows: \n"
                "    set PATH=%PATH%;C:path-to-your-folder \n \n"
                "Linux: \n"
                "    PATH=$PATH:/path/toyour/folder/ \n"
            )
        else:
            raise
