from art_gallery_window import ArtGalleryWindow
from art_gallery_db import ArtGalleryDatabase
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    main_program_window = ArtGalleryWindow(window)
    window.title("Art Gallery")
    window.geometry("1220x600")
    window.mainloop()
    db = "art_gallery.db"
    with ArtGalleryDatabase(db) as conn_cursor:
        # print(conn_cursor.execute("select sqlite_version();").fetchall()[0][0])
        conn_cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
        artistid integer PRIMARY KEY, name text, address text, town text, county text, postcode
        text); """)
        conn_cursor.execute("""CREATE TABLE IF NOT EXISTS Arts(
        pieceid integer PRIMARY KEY, artistid integer not null, title text not null, medium text not null, 
        price integer not null);
        """)
