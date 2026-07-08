import tkinter as tk


class HistoryManager:

    def __init__(self, parent):

        self.history = []

        self.listbox = tk.Listbox(
            parent,
            width=28,
            font=("Arial", 12)
        )

        self.listbox.pack(
            side="right",
            fill="y",
            padx=5,
            pady=5
        )

    def add(self, expression, result):

        text = f"{expression} = {result}"

        self.history.append(text)

        self.listbox.insert(tk.END, text)

    def clear(self):

        self.history.clear()

        self.listbox.delete(0, tk.END)