from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.goto(x = 0,y = 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Score: {self.score} Highest Score: {self.highest_score} ",move= False,align= ALIGNMENT,font= FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     # self.clear()
    #     self.color("red")
    #     self.write(arg= f"Game Over!",move= False,align= ALIGNMENT,font= FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()