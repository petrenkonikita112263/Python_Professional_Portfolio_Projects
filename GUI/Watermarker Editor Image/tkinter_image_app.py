import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageDraw


def copyright_apply(text):
    image_path = filedialog.askopenfilename(filetypes=[("Image File", ".png", ".jpg")])
    photo = Image.open(image_path)
    w, h = photo.size

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    text = "© " + text + "   "
    text_w, text_h = drawing.textsize(text)
    text_position = w - text_w, (h - text_h) - 50
    c_text = Image.new('RGB', (text_w, (text_h)), color='#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text)
    c_text.putalpha(100)

    photo.paste(c_text, text_position, c_text)
    photo.save("./sealed_image.png")


class TkinterImageApplication(tk.Frame):
    def __init__(self, author_text, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(author_text)

    def create_widgets(self, text):
        self.edit_image = tk.Button(self)
        self.edit_image["text"] = "Verify Image"
        self.edit_image["command"] = copyright_apply(text)
        self.edit_image.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
