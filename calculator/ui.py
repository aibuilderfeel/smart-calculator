import tkinter as tk

from calculator.engine import CalculatorEngine
from calculator.menu import MenuManager
from calculator.history import HistoryManager
from calculator.keyboard import KeyboardManager


class CalculatorUI:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Smart Calculator Pro")
        self.window.geometry("650x600")
        self.window.resizable(False, False)

        self.expression = ""

        MenuManager.create(self.window, self)

        KeyboardManager.bind(self.window, self)
        self.window.bind("<Control-c>", self.copy_result)
        self.display = tk.Entry(
            self.window,
            font=("Arial", 24),
            justify="right",
            bd=10
        )

        self.display.pack(fill="x", padx=10, pady=10)

        body = tk.Frame(self.window)
        body.pack(expand=True, fill="both")

        left = tk.Frame(body)
        left.pack(side="left", expand=True, fill="both")

        right = tk.Frame(body)
        right.pack(side="right", fill="y")

        self.history = HistoryManager(right, self)

        self.create_buttons(left)

    def create_buttons(self, parent):

        buttons = [
            ["C", "DEL", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "", ""]
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                if text == "":
                    continue

                if text == "=":
                    command = self.calculate

                elif text == "C":
                    command = self.clear

                elif text == "DEL":
                    command = self.delete

                else:
                    command = lambda t=text: self.press(t)

                button = tk.Button(
                    parent,
                    text=text,
                    font=("Arial", 20),
                    command=command,
                    width=5,
                    height=2
                )

                if text == "=":
                    button.config(bg="#4CAF50", fg="white")

                elif text == "C":
                    button.config(bg="#F44336", fg="white")

                elif text == "DEL":
                    button.config(bg="#FF9800", fg="white")

                button.grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=3,
                    pady=3
                )
                button.bind(
                    "<Enter>",
                    lambda event, b=button: b.config(relief="raised")
                )

                button.bind(
                    "<Leave>",
                    lambda event, b=button: b.config(relief="groove")
                )

                button.config(relief="groove")
        for i in range(5):
            parent.grid_rowconfigure(i, weight=1)

        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)

    def press(self, value):

        self.expression += str(value)

        self.update_display()

    def update_display(self):

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):

        expression = self.expression

        result = CalculatorEngine.calculate(expression)

        self.expression = result

        self.update_display()

        if expression and result not in ("Error", "Cannot divide by zero"):

            self.history.add(expression, result)

            self.display.selection_range(0, tk.END)

            self.display.icursor(tk.END)

    def clear(self):

        self.expression = ""

        self.update_display()

    def delete(self):

        self.expression = self.expression[:-1]

        self.update_display()

    def copy_result(self, event=None):

        self.window.clipboard_clear()

        self.window.clipboard_append(self.expression)

        self.window.update()

    def run(self):

        self.window.mainloop()


def run():

    app = CalculatorUI()

    app.run()