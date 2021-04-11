import turtle
import winsound

wn = turtle.Screen()
wn.title("Classic Pong")
wn.bgcolor("#000033")
wn.setup(width=800, height=600)
wn.tracer(0)  # Stops window from updating: Speed up our game

# Paddle A
paddle_a = turtle.Turtle()
# module #Class
paddle_a.speed(0)  # speed of animation 0: maximum
paddle_a.shape("square")  # Originally 20px*20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # Bcoz originally Turtles draw a line as they move
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx: float = 0.25
ball.dy: float = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Times new Roman", 24, "normal"))

score_a=0
score_b=0
# Function
def paddle_a_up():
    y = paddle_a.ycor()  # .ycor: turtle module property;returns y coordinate
    y += 60
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)


def paddle_b_up():
        y = paddle_b.ycor()  # .ycor: turtle module property;returns y coordinate
        y += 60
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)


# Keyboard Binding: listen to keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Times new Roman", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Times new Roman", 24, "normal"))


    # When Paddle and Ball collide
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
