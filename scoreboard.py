from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
