import turtle

# Paddle A
paddle_a = turtle.Turtle()

# Speed of animation set to max possible speed
paddle_a.speed(0)

# Give paddle a built in shape.
# default shape is 20px, 20px
paddle_a.shape("square")

# stretching is multiplying the current size by a factor
paddle_a.shapesize(stretch_wid=3, stretch_len=1)

# Paddle A colour
paddle_a.color("white")

# Turtles draw a line. We don't need that here.
paddle_a.penup()

# The centre of the screen is (0,0)
# Paddle A is on the left hand side which is (-x,0)
paddle_a.goto(-350, 0)
