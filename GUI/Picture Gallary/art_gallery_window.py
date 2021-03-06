import tkinter as tk
from tkinter import END
from art_gallery_db import ArtGalleryDatabase


def _create_tables(db_file: str) -> None:
    """ In first run creates the tables if they're not existed by custom class, otherwise skips its creation. """
    with ArtGalleryDatabase(db_file) as conn_cursor:
        conn_cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
        artistid integer PRIMARY KEY, name text, address text, town text, county text, postcode
        text); """)
        conn_cursor.execute("""CREATE TABLE IF NOT EXISTS Arts(
        pieceid integer PRIMARY KEY, artistid integer not null, title text not null, medium text not null, 
        price integer not null);
        """)


class ArtGalleryWindow(tk.Frame):
    """ The class that is responsible for displaying the window and running methods. """

    def __init__(self, parent, db_file: str):
        """
        Initialize the ArtGalleryWindow class with a current object of the root window and database file.
        :param parent: a widget that acts as the parent of the current object
        :param db_file: database file
        """
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
                                           command=self.add_artist)
        self.add_artist_button.place(x=110, y=80, width=130, height=25)
        self.clear_artist_button = tk.Button(text="Clear Artist's entries",
                                             command=self.clear_artist_entries)
        self.clear_artist_button.place(x=250, y=80, width=130, height=25)
        self.artist_id_label = tk.Label(text="Artist ID: ")
        self.artist_id_label.place(x=30, y=120, width=80, height=25)

        # TODO 1: Replaced getting artist id from user's enter by option menu from database.
        self.artist_id = tk.Entry(text="")
        self.artist_id.place(x=110, y=120, width=50, height=25)

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
        self.add_art_button = tk.Button(text="Add Art",
                                        command=self.add_art)
        self.add_art_button.place(x=110, y=150, width=130, height=25)
        self.clear_art_button = tk.Button(text="Clear Art's entries",
                                          command=self.clear_art_entries)
        self.clear_art_button.place(x=250, y=150, width=130, height=25)

        """This area will display the selected information from database and clear it by pressing the button"""
        self.display_output = tk.Listbox()
        self.display_output.place(x=10, y=200, width=1000, height=350)
        self.clear_output = tk.Button(text="Clear Output",
                                      command=self.clear_window)
        self.clear_output.place(x=1020, y=200, width=155, height=25)

        """Different option to select the data from database"""
        self.get_all_artists = tk.Button(text="View All Artists",
                                         command=self.view_all_artists)
        self.get_all_artists.place(x=1020, y=230, width=155, height=25)
        self.get_all_arts = tk.Button(text="View All Arts",
                                      command=self.view_all_arts)
        self.get_all_arts.place(x=1020, y=260, width=155, height=25)

        """Search by artist name"""
        self.find_artist = tk.Entry(text="")
        self.find_artist.place(x=1020, y=300, width=50, height=25)
        self.find_artist_button = tk.Button(text="Search by Artist",
                                            command=self.search_by_artist)
        self.find_artist_button.place(x=1075, y=300, width=100, height=25)

        """Search by type of paint grade"""
        self.type_paint_grade = tk.StringVar(parent)
        self.selected_paint_grade = tk.OptionMenu(parent, self.type_paint_grade, "Oil", "Watercolour", "Ink", "Acrylic")
        self.selected_paint_grade.place(x=1020, y=330, width=100, height=25)
        self.find_paint_grade_button = tk.Button(text="Search",
                                                 command=self.search_by_paint_type)
        self.find_paint_grade_button.place(x=1125, y=330, width=50, height=25)

        """Search by price"""
        self.min_price_label = tk.Label(text="Min: ")
        self.min_price_label.place(x=1020, y=360, width=75, height=25)
        self.max_price_label = tk.Label(text="Max: ")
        self.max_price_label.place(x=1100, y=360, width=75, height=25)
        self.min_price_value = tk.Entry(text="")
        self.min_price_value.place(x=1020, y=380, width=75, height=25)
        self.max_price_value = tk.Entry(text="")
        self.max_price_value.place(x=1100, y=380, width=75, height=25)
        self.search_price_button = tk.Button(text="Search by Price",
                                             command=self.search_by_price)
        self.search_price_button.place(x=1020, y=410, width=155, height=25)

        """Buy the picture from the art"""
        self.selected_art = tk.Entry(text="")
        self.selected_art.place(x=1020, y=450, width=50, height=25)
        self.sold_button = tk.Button(text="Sold",
                                     command=self.sold_picture)
        self.sold_button.place(x=1075, y=450, width=100, height=25)

        """Create the tables"""
        _create_tables(db_file)

    def clear_artist_entries(self) -> None:
        """
        Deletes all the input values from the artist's entries.
        :return: None
        """
        self.artist_name.delete(0, END)
        self.artist_address.delete(0, END)
        self.artist_town.delete(0, END)
        self.artist_country.delete(0, END)
        self.artist_postcode.delete(0, END)
        self.artist_name.focus()
        self.add_artist_button["state"] = "normal"

    def clear_art_entries(self) -> None:
        """
        Deletes all the input values from the art's entries and sets the option menu to empty string.
        :return: None
        """
        self.artist_id.delete(0, END)
        self.art_title.delete(0, END)
        self.paint_grade.set("")
        self.art_price.delete(0, END)
        self.add_art_button["state"] = "normal"

    def clear_window(self) -> None:
        """
        Method that clears the screen that displays selected data.
        :return: None
        """
        self.display_output.delete(0, END)

    def add_artist(self) -> None:
        """
        Method that allows user to add the new artist into db.
        :return: None
        """
        new_name = self.artist_name.get()
        new_address = self.artist_address.get()
        new_town = self.artist_town.get()
        new_country = self.artist_country.get()
        new_postcode = self.artist_postcode.get()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""INSERT INTO Artists (name, address, town, county, postcode)
                VALUES (?, ?, ?, ?, ?)""", (new_name, new_address, new_town, new_country, new_postcode))
        self.add_artist_button["state"] = "disabled"

    def view_all_artists(self) -> None:
        """
        Prints the Artists table into window.
        :return: None
        """
        self.clear_window()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""SELECT * FROM Artists""")
            for row in conn_cursor.fetchall():
                data_record = f"ArtistId: {row[0]}          Name: {row[1]}           Address: {row[2]}" \
                              f"            Town: {row[3]}          Country: {row[4]}           Postcode: {row[5]}\n"""
                self.display_output.insert(END, data_record)

    def add_art(self) -> None:
        """
        Method that allows user to add the new art into db.
        :return: None
        """
        new_artist_id = self.artist_id.get()
        new_title = self.art_title.get()
        new_paint_grade = self.paint_grade.get()
        new_price = self.art_price.get()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""INSERT INTO Arts (artistID, title, medium, price)
                VALUES (?, ?, ?, ?)""", (new_artist_id, new_title, new_paint_grade, new_price))
        self.add_art_button["state"] = "disabled"

    def view_all_arts(self) -> None:
        """
        Prints the Arts table into window.
        :return: None
        """
        self.clear_window()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""SELECT * FROM Arts""")
            for row in conn_cursor.fetchall():
                data_record = f"ArtId: {row[0]}          ArtistId: {row[1]}           Title: {row[2]}" \
                              f"            Medium: {row[3]}          Price: {row[4]}\n"""
                self.display_output.insert(END, data_record)

    def search_by_artist(self):
        """
        User enters the artist name to view all his|her arts.
        :return: None
        """
        artist_name = self.find_artist.get()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""SELECT pieceid, title, medium, price FROM Arts 
            WHERE artistid = (SELECT artistid FROM Artists WHERE name LIKE ?)""", [artist_name])
            for row in conn_cursor.fetchall():
                result = f"ArtId: {row[0]}           Title: {row[1]}" \
                         f"            Medium: {row[2]}          Price: {row[3]}\n"""
                self.display_output.insert(END, result)
        self.find_artist.delete(0, END)
        self.find_artist.focus()

    def search_by_price(self) -> None:
        """
        User sets the low and high price and finds out what pictures get under this range.
        :return: None
        """
        min_price = self.min_price_value.get()
        max_price = self.max_price_value.get()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""SELECT Arts.pieceid, Artists.name, Arts.title, Arts.medium, Arts.price
                                    FROM Artists, Arts 
                                    WHERE Artists.artistid = Arts.artistid AND 
                                    Arts.price BETWEEN ? AND ?""", [min_price, max_price])
            for row in conn_cursor.fetchall():
                result = f"ArtId: {row[0]}           Artist name: {row[1]}          Title: {row[2]}" \
                         f"            Medium: {row[3]}          Price: {row[4]}\n"""
                self.display_output.insert(END, result)
        self.min_price_value.delete(0, END)
        self.max_price_value.delete(0, END)

    def search_by_paint_type(self) -> None:
        """
        From list menu the user chooses the type of paint's grade and finds what pictures
        are in db with this grade.
        :return: None
        """
        selected_type = self.type_paint_grade.get()
        with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
            conn_cursor.execute("""SELECT Arts.pieceid, Artists.name, Arts.title, Arts.medium, Arts.price 
                                    FROM Artists, Arts 
                                    WHERE Artists.artistid = Arts.artistid AND Arts.medium = ?""", [selected_type])
            for row in conn_cursor.fetchall():
                result = f"ArtId: {row[0]}           Artist name: {row[1]}          Title: {row[2]}" \
                         f"            Medium: {row[3]}          Price: {row[4]}\n"""
                self.display_output.insert(END, result)
        self.type_paint_grade.set("")

    def sold_picture(self) -> None:
        """
        By entering the art id, the selected pictures stores into file and deleted from db.
        :return: None
        """
        with open("sold_pictures.txt", "a") as file:
            selected_picture = self.selected_art.get()
            with ArtGalleryDatabase("art_gallery.db") as conn_cursor:
                conn_cursor.execute("""SELECT * FROM Arts WHERE pieceid = ?""", [selected_picture])
                for row in conn_cursor.fetchall():
                    data_record = f"ArtId: {row[0]}          ArtistId: {row[1]}           Title: {row[2]}" \
                                  f"            Medium: {row[3]}          Price: {row[4]}\n"""
                    file.write(data_record)
                conn_cursor.execute("""DELETE FROM Arts WHERE pieceid = ?""", [selected_picture])
        self.selected_art.delete(0, END)
