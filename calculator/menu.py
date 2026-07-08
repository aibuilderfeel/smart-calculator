import tkinter as tk

from calculator.dialogs import DialogManager
from calculator.theme import ThemeManager


class MenuManager:

    @staticmethod
    def create(window, app):

        menu_bar = tk.Menu(window)

        # File
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=window.quit)

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        # View
        view_menu = tk.Menu(menu_bar, tearoff=0)

        view_menu.add_command(
            label="Light Mode",
            command=lambda: ThemeManager.light(app)
        )

        view_menu.add_command(
            label="Dark Mode",
            command=lambda: ThemeManager.dark(app)
        )

        menu_bar.add_cascade(
            label="View",
            menu=view_menu
        )

        # Help
        help_menu = tk.Menu(menu_bar, tearoff=0)

        help_menu.add_command(
            label="About",
            command=DialogManager.show_about
        )

        menu_bar.add_cascade(
            label="Help",
            menu=help_menu
        )

        window.config(menu=menu_bar)