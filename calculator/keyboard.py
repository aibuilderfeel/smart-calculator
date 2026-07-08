class KeyboardManager:

    @staticmethod
    def bind(window, app):

        window.bind("<Return>", lambda event: app.calculate())

        window.bind("<BackSpace>", lambda event: app.delete())

        window.bind("<Escape>", lambda event: app.clear())

        for key in "0123456789":
            window.bind(key, lambda event, k=key: app.press(k))

        for key in "+-*/.":
            window.bind(key, lambda event, k=key: app.press(k))
        window.bind("<Delete>", lambda event: app.clear())