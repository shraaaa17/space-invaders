# result_window.py

import tkinter as tk

class ResultWindow:
    def __init__(self, username, score):
        self.username = username
        self.score = score

        self.root = tk.Tk()
        self.root.title("Game Over")
        self.root.geometry("300x200")

        self.label_username = tk.Label(self.root, text="Username: " + self.username)
        self.label_username.pack()

        self.label_score = tk.Label(self.root, text="Score: " + str(self.score))
        self.label_score.pack()

        self.root.mainloop()
