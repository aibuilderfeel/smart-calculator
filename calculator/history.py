import tkinter as tk
from pathlib import Path


class HistoryManager:

    FILE_NAME = Path("history.txt")

    def __init__(self, parent, app):

        self.app = app
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

        self.listbox.bind("<Double-Button-1>", self.load_expression)

        self.menu = tk.Menu(self.listbox, tearoff=0)
        self.menu.add_command(
            label="🗑 Clear History",
            command=self.clear
        )

        self.listbox.bind("<Button-3>", self.show_menu)

        self.load_file()

    def add(self, expression, result):

        text = f"{expression} = {result}"

        self.history.append(text)

        self.listbox.insert(tk.END, text)

        with open(self.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def clear(self):

        self.history.clear()

        self.listbox.delete(0, tk.END)

        self.FILE_NAME.write_text("", encoding="utf-8")

    def show_menu(self, event):

        self.menu.post(event.x_root, event.y_root)

    def load_expression(self, event):

        if not self.listbox.curselection():
            return

        text = self.listbox.get(self.listbox.curselection())

        expression = text.split("=")[0].strip()

        self.app.expression = expression

        self.app.update_display()

    def load_file(self):

        if not self.FILE_NAME.exists():
            return

        with open(self.FILE_NAME, "r", encoding="utf-8") as file:

            for line in file:

                text = line.strip()

                if text:

                    self.history.append(text)

                    self.listbox.insert(tk.END, text)