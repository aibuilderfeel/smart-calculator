import tkinter as tk


class ThemeManager:

    @staticmethod
    def light(app):

        app.window.configure(bg="SystemButtonFace")

        app.display.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        for widget in app.window.winfo_children():
            ThemeManager._light(widget)

    @staticmethod
    def dark(app):

        app.window.configure(bg="#1e1e1e")

        app.display.configure(
            bg="#2d2d2d",
            fg="white",
            insertbackground="white"
        )

        for widget in app.window.winfo_children():
            ThemeManager._dark(widget)

    @staticmethod
    def _dark(widget):

        try:
            if isinstance(widget, tk.Frame):
                widget.configure(bg="#1e1e1e")

            elif isinstance(widget, tk.Button):
                widget.configure(
                    bg="#3c3f41",
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white"
                )

            elif isinstance(widget, tk.Listbox):
                widget.configure(
                    bg="#2d2d2d",
                    fg="white",
                    selectbackground="#555555"
                )

        except:
            pass

        for child in widget.winfo_children():
            ThemeManager._dark(child)

    @staticmethod
    def _light(widget):

        try:
            if isinstance(widget, tk.Frame):
                widget.configure(bg="SystemButtonFace")

            elif isinstance(widget, tk.Button):
                widget.configure(
                    bg="SystemButtonFace",
                    fg="black"
                )

            elif isinstance(widget, tk.Listbox):
                widget.configure(
                    bg="white",
                    fg="black"
                )

        except:
            pass

        for child in widget.winfo_children():
            ThemeManager._light(child)