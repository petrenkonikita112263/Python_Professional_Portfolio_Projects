import tkinter as tk


class ArtGalleryWindow(tk.Frame):
    """Tkinter window"""

    def __init__(self, parent):
        """From superclass created the actual frame"""
        tk.Frame.__init__(self, parent)
        """Filling the window with labels, buttons and etc"""
        self.info_label = tk.Label(text="Please enter the information about artist and its arts")
        self.info_label.place(x=410, y=10, width=300, height=25)
        self.artist_name_label = tk.Label(text="Artist name: ")
        self.artist_name_label.place(x=30, y=40, width=80, height=25)
        self.artist_name = tk.Entry(text="")
        self.artist_name.place(x=110, y=40, width=200, height=25)
        self.artist_name.focus()
        self.artist_address_label = tk.Label(text="Artist address: ")
        self.artist_address_label.place(x=310, y=40, width=80, height=25)
        self.artist_address = tk.Entry(text="")
        self.artist_address.place(x=390, y=40, width=200, height=25)
        self.artist_town_label = tk.Label(text="Town(city): ")
        self.artist_town_label.place(x=590, y=40, width=80, height=25)
        self.artist_town = tk.Entry(text="")
        self.artist_town.place(x=670, y=40, width=100, height=25)
        self.artist_country_label = tk.Label(text="County: ")
        self.artist_country_label.place(x=770, y=40, width=80, height=25)
        self.artist_country = tk.Entry(text="")
        self.artist_country.place(x=850, y=40, width=100, height=25)
        self.artist_postcode_label = tk.Label(text="Postcode: ")
        self.artist_postcode_label.place(x=950, y=40, width=80, height=25)
        self.artist_postcode = tk.Entry(text="")
        self.artist_postcode.place(x=1030, y=40, width=100, height=25)
        self.add_artist_button = tk.Button(text="Add Artist",
                                           command="functions that add artist")
        self.add_artist_button.place(x=110, y=80, width=130, height=25)
        self.clear_artist_button = tk.Button(text="Clear Artist's entries",
                                             command="clear all the entries about artist")
        self.clear_artist_button.place(x=250, y=80, width=130, height=25)
        self.art_id_label = tk.Label(text="Artist ID: ")
        self.art_id_label.place(x=30, y=120, width=80, height=25)
        self.art_id = tk.Entry(text="")
        self.art_id.place(x=110, y=120, width=50, height=25)
        self.art_title_label = tk.Label(text="Title: ")
        self.art_title_label.place(x=200, y=120, width=80, height=25)
        self.art_title = tk.Entry(text="")
        self.art_title.place(x=280, y=120, width=280, height=25)
        self.paint_grade_label = tk.Label(text="Paint grade: ")
        self.paint_grade_label.place(x=590, y=120, width=80, height=25)
        self.paint_grade = tk.StringVar(parent)
        self.paint_grade_option = tk.OptionMenu(parent, self.paint_grade, "Oil", "Watercolour", "Ink", "Acrylic")
        self.paint_grade_option.place(x=670, y=120, width=100, height=25)
        self.art_price_label = tk.Label(text="Price:")
        self.art_price_label.place(x=770, y=120, width=80, height=25)
        self.art_price = tk.Entry(text="")
        self.art_price.place(x=850, y=120, width=100, height=25)
        self.add_art_button = tk.Button(text="Add Piece",
                                        command="functions that add art into gallery")
        self.add_art_button.place(x=110, y=150, width=130, height=25)
        self.clear_art_button = tk.Button(text="Clear Piece",
                                          command="clear all the entries about art")
        self.clear_art_button.place(x=250, y=150, width=130, height=25)
        """This area will display the selected information from database and clear it by pressing the button"""
        self.display_output = tk.Listbox()
        self.display_output.place(x=10, y=200, width=1000, height=350)
        self.clear_output = tk.Button(text="Clear Output",
                                      command="function that clears the output info")
        self.clear_output.place(x=1020, y=200, width=155, height=25)
