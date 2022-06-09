import tkinter
import random


class Canvas:
    pass


class TicTacToe(tkinter.Canvas):

    def __init__(self, window):
        self.window = window
        super().__init__(window, width=300, height=300)
        self.state = [None, ] * 9
        self.bind('<Button-1>', self.click)

    """Нанесение разметки поля"""
    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')

        self.create_line(200, 0, 200, 300, fill='grey')

        self.create_line(0, 100, 300, 100, fill='grey')

        self.create_line(0, 200, 300, 200, fill='grey')

    """Вывод 'X' по координатам нажатия"""
    def add_x(self, column, row):
        self.create_line(
            20 + column * 100,
            20 + row * 100,
            80 + column * 100,
            80 + row * 100,
            width=5,
            fill='blue'
        )
        self.create_line(
            20 + column * 100,
            80 + row * 100,
            80 + column * 100,
            20 + row * 100,
            width=5,
            fill='blue'
        )

    """Вывод 'O' по координатам нажатия"""
    def add_o(self, column, row):
        self.create_oval(
            20 + column * 100,
            20 + row * 100,
            80 + column * 100,
            80 + row * 100,
            width=5,
            outline='red'
        )

    """Считывание координат нажатия"""
    def click(self, event):
        column = int(event.x / 100)
        row = int(event.y / 100)
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(column, row)
            self.bot_move()
            self.get_winner()



    """Простой соперник ходит случайно"""
    def bot_move(self):
        """Проверка на наличие свободных ячеек"""
        if None not in self.state:
            game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
            game.create_text(150, 150, text="Draw", fill="DarkOrange3", font=("Times", 54))

        else:
            while True:

                i = random.randint(0, 8)
                if self.state[i] == None:
                    self.state[i] = "o"

                    row = i // 3
                    column = i - 3 * row
                    self.add_o(column, row)
                    break


    """Выявление победителя"""
    def get_winner(self):

        """Проверка горизонталей"""
        for i in range(0, 7, 3):
            if self.state[i] == self.state[i + 1] == self.state[i + 2] == "x":
                game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
                game.create_text(150, 150, text="X Win", fill="DarkOrange3", font=("Times", 54))


            elif self.state[i] == self.state[i + 1] == self.state[i + 2] == "o":
                game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
                game.create_text(150, 150, text="X Win", fill="DarkOrange3", font=("Times", 54))

        """Проверка вертикалей"""
        for i in range(0, 3):
            if self.state[i] == self.state[i + 3] == self.state[i + 6] == "x":
                game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
                game.create_text(150, 150, text="X Win", fill="DarkOrange3", font=("Times", 54))

            elif self.state[i] == self.state[i + 3] == self.state[i + 6] == "o":
                game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
                game.create_text(150, 150, text="O Win", fill="DarkOrange3", font=("Times", 54))

        """Проверка диагоналей"""
        if self.state[0] == self.state[4] == self.state[8] == "x":
            game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
            game.create_text(150, 150, text="X Win", fill="DarkOrange3", font=("Times", 54))

        elif self.state[2] == self.state[4] == self.state[6] == "x":
            game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
            game.create_text(150, 150, text="X Win", fill="DarkOrange3", font=("Times", 54))

        elif self.state[0] == self.state[4] == self.state[8] == "o":
            game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
            game.create_text(150, 150, text="O Win", fill="DarkOrange3", font=("Times", 54))

        elif self.state[2] == self.state[4] == self.state[6] == "o":
            game.create_rectangle(-50, -50, 350, 350, fill="orange", outline="DarkOrange3")
            game.create_text(150, 150, text="O Win", fill="DarkOrange3", font=("Times", 54))




tk_window = tkinter.Tk()
game = TicTacToe(tk_window)
game.pack()
game.draw_lines()
tk_window.mainloop()
