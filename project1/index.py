import turtle

wn = turtle.Screen()
wn.title("Zipporia")
wn.setup(width=800, height=600)
wn.bgcolor("yellow green")
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0   ||  Player B: 0", align="center", font=("Courier", 15, "bold"))

# function
def paddle_a_up():
    y = paddle_a.ycor()  # ycor = returns the y coordinate
    y += 10
    paddle_a.sety(y)  # set y to a new y position


def paddle_a_down():
    y = paddle_a.ycor()  # ycor = returns the y coordinate
    y -= 10
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # ycor = returns the y coordinate
    y += 10
    paddle_b.sety(y)  # set y to a new y position


def paddle_b_down():
    y = paddle_b.ycor()  # ycor = returns the y coordinate
    y -= 10
    paddle_b.sety(y)


# keyboard binding
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

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write("Player A: {}   ||  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write("Player A: {}   ||  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "bold"))

    if (ball.xcor() > 330 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 63 and ball.ycor() > paddle_b.ycor() -63:
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 63 and ball.ycor() > paddle_a.ycor() -63:
        ball.setx(-330)
        ball.dx *= -1

