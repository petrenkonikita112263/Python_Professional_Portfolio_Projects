import tkinter as tk


class ArtGalleryWindow(tk.Frame):
    """Tkinter window"""

    def __init__(self, parent):
        """From superclass created the actual frame"""
        tk.Frame.__init__(self, parent)
        """Filling the window with labels, buttons and etc"""
        self.info_label = tk.Label(text="Please enter the information about artist")
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
