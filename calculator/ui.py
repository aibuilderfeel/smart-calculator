import tkinter as tk

from calculator.engine import CalculatorEngine


class CalculatorUI:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Smart Calculator Pro")
        self.window.geometry("400x600")
        self.window.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            self.window,
            font=("Arial", 24),
            justify="right",
            bd=10
        )

        self.display.pack(fill="x", padx=10, pady=10)

        self.create_buttons()

        # 키보드 지원
        self.window.bind("<Return>", lambda event: self.calculate())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        self.window.bind("<Escape>", lambda event: self.clear())

    # --------------------
    # 버튼 생성
    # --------------------

    def create_buttons(self):

        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")

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

                    frame,

                    text=text,

                    font=("Arial", 20),

                    command=command

                )

                button.grid(

                    row=r,

                    column=c,

                    sticky="nsew",

                    padx=3,

                    pady=3

                )

        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    # --------------------
    # 버튼 입력
    # --------------------

    def press(self, value):

        self.expression += str(value)

        self.update_display()

    # --------------------
    # 화면 업데이트
    # --------------------

    def update_display(self):

        self.display.delete(0, tk.END)

        self.display.insert(tk.END, self.expression)

    # --------------------
    # 계산
    # --------------------

    def calculate(self):

        result = CalculatorEngine.calculate(self.expression)

        self.expression = result

        self.update_display()

    # --------------------
    # 전체 삭제
    # --------------------

    def clear(self):

        self.expression = ""

        self.update_display()

    # --------------------
    # 한 글자 삭제
    # --------------------

    def delete(self):

        self.expression = self.expression[:-1]

        self.update_display()

    # --------------------
    # 실행
    # --------------------

    def run(self):

        self.window.mainloop()


def run():

    app = CalculatorUI()

    app.run()