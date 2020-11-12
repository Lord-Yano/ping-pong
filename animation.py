import paddles
import window

# Function to move paddle A up and down


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


# Function to move paddle B up and down
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
