from art_gallery_window import ArtGalleryWindow
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    main_program_window = ArtGalleryWindow(window)
    window.title("Art Gallery")
    window.geometry("1220x600")
    window.mainloop()
