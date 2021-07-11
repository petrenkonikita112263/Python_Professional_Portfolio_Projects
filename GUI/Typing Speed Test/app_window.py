import random
import tkinter as tk
from tkinter import messagebox

from words import word_list

score = 0
miss_words = 0
wpm_value = 0


def retrieve_word(words) -> str:
    typed_word = random.choice(words)
    return typed_word


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.title = tk.Label(self.frame, text="TEST YOUR TYPING SPEED\n\n\n", font=("Comic Sans", "24", "bold"))
        self.title.pack()

        self.timer = tk.Label(self.frame, text="Time left: 60\n", font=("Comic Sans", "20"))
        self.timer.pack()

        self.timer_value = tk.IntVar(self.frame, value=60)

        self.label = tk.Label(self.frame, text=f"{retrieve_word(word_list)}\n", fg="blue",
                              font=("Comic Sans", "16", "italic"))
        self.label.pack()

        self.user_entry = tk.Entry(self.frame, font=("Comic Sans", "16", "italic"), justify="center")
        self.user_entry.pack()

        self.detail_label = tk.Label(self.frame, text="Type here the word that you see on the screen. And press ENTER",
                                     fg="dark grey", font=("Arial", 14, "italic bold"))
        self.detail_label.pack()

        self.score_label = tk.Label(self.frame, text=f"Your Score: {score}", fg="red", font=("Comic Sans", "20"))
        self.score_label.pack()

        self.result_label = tk.Label(self.frame, fg="red", font=("Comic Sans", "20"))
        self.result_label.pack()

        self.master.bind("<Return>", self.start_app)

    def start_app(self, event):
        global score, wpm_value, miss_words
        self.time()
        if self.user_entry.get() == self.label.cget("text"):
            score += len(self.user_entry.get())
            wpm_value = (score / 5) / 1
            self.score_label.config(text=f"Your WPM: {wpm_value}")
        else:
            miss_words += 1
        self.label.config(text=retrieve_word(word_list))
        self.user_entry.delete(0, "end")

    def time(self):
        global score, miss_words
        if self.timer_value.get() > 0:
            old_time = self.timer_value.get()
            self.timer_value.set(old_time - 1)
            new_time = self.timer_value.get()
            self.timer.config(text=f"Time left: {new_time}")
            self.timer.after(1000, self.time)
        else:
            self.result_label.config(
                text=f"Matched - {score} | Miss - {miss_words} | Total Score - {score - miss_words}")
            retry_again = messagebox.askretrycancel("Notification", "To try again press RETRY button")
            if retry_again is True:
                score = 0
                self.timer_value.set(60)
                self.timer.config(text="Time left: 60")
                self.user_entry.delete(0, "end")
                self.score_label.config(text=f"Your Score: {score}")
                self.result_label.config(text="")
