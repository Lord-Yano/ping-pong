import paddles
import window

# Functions to move paddle A up and down


def paddle_a_up():

    # Obtain the current cord of paddle a
    y = paddles.paddle_a.ycor()

    # Add or displace it by 20 upwards
    y += 20

    # Set the new y cord of paddle A to y
    paddles.paddle_a.sety(y)


def paddle_a_down():

    # Obtain the current cord of paddle a
    y = paddles.paddle_a.ycor()

    # Add or displace it by 20 upwards
    y -= 20

    # Set the new y cord of paddle A to y
    paddles.paddle_a.sety(y)


# Functions to move paddle B up and down


def paddle_b_up():

    # Obtain the current cord of paddle a
    y = paddles.paddle_b.ycor()

    # Add or displace it by 20 upwards
    y += 20

    # Set the new y cord of paddle A to y
    paddles.paddle_b.sety(y)


def paddle_b_down():

    # Obtain the current cord of paddle a
    y = paddles.paddle_b.ycor()

    # Add or displace it by 20 upwards
    y -= 20

    # Set the new y cord of paddle A to y
    paddles.paddle_b.sety(y)


# Ball movement
# Separated into 2 parts - x & y movement.
# dx is the change in x, in this case by 2 pixels
# (+0.03) x and (+0.03) y means that the ball moves upwards and to the side simultaneoulsy (diagonally)
paddles.ball_a.dx = 0.03
paddles.ball_a.dy = 0.03


# Keyboard Binding
# Tells it to listen for keyboard input
window.wn.listen()

# On keypress of w, call function paddle_f()_orientation

# Paddle A up and down
window.wn.onkeypress(paddle_a_up, "w")
window.wn.onkeypress(paddle_a_down, "s")

# Paddle B up and down
window.wn.onkeypress(paddle_b_up, "i")
window.wn.onkeypress(paddle_b_down, "k")


# Function to handle ball animation


def ball_animation():
    # Bordering the ball

    # The screen is h-600px which is 300px from the centre.
    # The screen is w-800px which is 400px from the centre.
    # The ball is 20x20 pixels which means that 10px is on either side of the half mark.

    # y is height
    # Boundary upwards
    if paddles.ball_a.ycor() > 290:
        paddles.ball_a.sety(290)
        paddles.ball_a.dy *= -1

    # Boundary downwards
    if paddles.ball_a.ycor() < -290:
        paddles.ball_a.sety(-290)
        paddles.ball_a.dy *= -1

    # x is the width
    # Boundary on the right side
    if paddles.ball_a.xcor() > 390:
        paddles.ball_a.setx(390)
        paddles.ball_a.dx *= -1

    # Boundary on the left side
    if paddles.ball_a.xcor() < -390:
        paddles.ball_a.setx(-390)
        paddles.ball_a.dx *= -1
