import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# def left():
#     snakes[0].setheading(90)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

race_on = True
while race_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # race_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    #if head collide with any segment of the body then game over
    for tail in snake.snakes[1:]:
        if tail == snake.head:
            pass
        if snake.head.distance(tail) <10:
            # race_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
screen.exitonclick()