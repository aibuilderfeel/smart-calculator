class KeyboardManager:

    @staticmethod
    def bind(window, app):

        window.bind("<Return>", lambda event: app.calculate())

        window.bind("<BackSpace>", lambda event: app.delete())

        window.bind("<Escape>", lambda event: app.clear())