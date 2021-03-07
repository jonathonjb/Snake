from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

gameIsOn = False

def startGame():
    global gameIsOn
    gameIsOn = True
    while (gameIsOn):
        snake.move()
        screen.update()
        time.sleep(0.1)

        if snake.head.distance(food) <= 15:
            food.spawn()
            scoreboard.increaseScore()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.gameOver()
            gameIsOn = False

        for segment in snake.segments[1:]:
            if (snake.head.distance(segment) < 10):
                scoreboard.gameOver()
                gameIsOn = False


screen.onkeypress(startGame)

screen.exitonclick()