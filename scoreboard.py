from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.level = self.level + 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

