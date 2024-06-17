from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision to the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    #detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    if scoreboard.r_score == 10:
        scoreboard.clear()
        scoreboard.goto(0,0)
        scoreboard.write("Right Player wins",align="center", font=("Courier", 40, "normal"))
        game_is_on = False
    if scoreboard.l_score == 10:
        scoreboard.clear()
        scoreboard.goto(0,0)
        scoreboard.write("Left Player wins", align="center", font=("Courier", 40, "normal"))
        game_is_on = False


screen.exitonclick()
