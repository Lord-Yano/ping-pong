# Ping pong game using turtle module
# import ping_ball
import turtle
import paddles
import window
import animation


# Window
window.wn

# Paddle A
paddles.paddle_a

# Paddle B
paddles.paddle_b

# Ball A
paddles.ball_a

# main game loop
while True:
    window.wn.update()

    # This animation needs to be constantly "on" hence why it is placed in the main loop.
    # On iteration 1 - cord x is set to the current xcor + 2.
    # On iteration 2 - cord x is set to current xcor (iteration 1) + 2.
    # dx determines the "speed" with which the ball is displaced from the previous iteration.
    animation.paddles.ball_a.setx(paddles.ball_a.xcor() + paddles.ball_a.dx)
    animation.paddles.ball_a.sety(paddles.ball_a.ycor() + paddles.ball_a.dy)

    # Function that handles ball boundary
    animation.ball_animation()
