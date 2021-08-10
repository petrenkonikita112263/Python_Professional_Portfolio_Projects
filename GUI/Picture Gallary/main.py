import tkinter as tk

from art_gallery_window import ArtGalleryWindow

DATABASE = "art_gallery.db"

if __name__ == "__main__":
    window = tk.Tk()
    main_program_window = ArtGalleryWindow(window, DATABASE)
    window.title("Art Gallery")
    window.geometry("1220x600")
    window.mainloop()
