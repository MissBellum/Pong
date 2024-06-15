import time
from turtle import Screen
from ballpong import Ball
from paddlepong import Paddle
from scoreboardpong import Scoreboard

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-382.5, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.faster)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 310 or ball.distance(l_paddle) < 30 and ball.xcor() < -310:
        ball.bounce_x()

    # Detect when right paddle misses ball
    if ball.xcor() > 375:
        ball.reset_position()
        score.l_point()
    # Detect when left paddle misses ball
    if ball.xcor() < -382.5:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
