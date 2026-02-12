from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self, cause):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0,-30)
        self.write(arg=cause, align=ALIGNMENT, font=FONT)
