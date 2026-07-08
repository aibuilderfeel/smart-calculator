import tkinter as tk
from tkinter import messagebox


class DialogManager:

    @staticmethod
    def show_about():

        messagebox.showinfo(
            "About",
            "Smart Calculator Pro\n\n"
            "Version : 2.0\n\n"
            "Made with Python\n"
            "Developer : aibuilderfeel"
        )