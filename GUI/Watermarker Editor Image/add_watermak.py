from tkinter_image_app import tk, TkinterImageApplication

INPUT_PATH_IMAGE = "./logo.png"
OUTPUT_PATH_IMAGE = "./logo_watermark.png"
AUTHOR_MARK = "Dark Overmind"

root = tk.Tk()
root.wm_title("Watermarker Editor Image")
root.geometry("100x100")
app = TkinterImageApplication(INPUT_PATH_IMAGE, OUTPUT_PATH_IMAGE, AUTHOR_MARK, master=root)
app.mainloop()
