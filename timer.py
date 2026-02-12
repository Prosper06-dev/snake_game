from turtle import Turtle
import time

FONT = ("Arial", 80, "bold")
ALIGNMENT = "center"

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -40)
        self.count()

    def count(self):
        for number in range(4, 0, -1):
            self.write(f"{number}", align=ALIGNMENT, font=FONT)
            self.getscreen().update()
            time.sleep(1.0)
            self.clear()
        self.write("GO!", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()

