import tkinter as tk

from PIL import Image, ImageDraw


def copyright_apply(input_image_path, output_image_path, text):
    photo = Image.open(input_image_path)
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
    photo.save(output_image_path)


class TkinterImageApplication(tk.Frame):
    def __init__(self, input_image, output_image, author_text, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(input_image, output_image, author_text)

    def create_widgets(self, old_image, new_image, text):
        self.edit_image = tk.Button(self)
        self.edit_image["text"] = "Verify Image"
        self.edit_image["command"] = copyright_apply(old_image, new_image, text)
        self.edit_image.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
