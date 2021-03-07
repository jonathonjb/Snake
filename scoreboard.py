from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highScore = 0
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f'Score: {self.score} High Score: {self.highScore}', align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        if(self.score > self.highScore):
            self.highScore = self.score
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)