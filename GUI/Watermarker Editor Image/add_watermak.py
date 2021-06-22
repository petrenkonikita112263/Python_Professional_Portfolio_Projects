from tkinter_image_app import tk, TkinterImageApplication

AUTHOR_MARK = "Dark Overmind"

root = tk.Tk()
root.wm_title("Watermarker Editor Image")
root.geometry("100x100")
app = TkinterImageApplication(AUTHOR_MARK, master=root)
app.mainloop()
