import turtle

# **Paddle A**
paddle_a = turtle.Turtle()

# Speed of animation set to max possible speed
paddle_a.speed(0)

# Give paddle a built in shape.
# default shape is 20px, 20px
paddle_a.shape("square")

# stretching is multiplying the current size by a factor
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle A colour
paddle_a.color("white")

# Turtles draw a line. We don't need that here.
paddle_a.penup()

# The centre of the screen is (0,0)
# Paddle A is on the left hand side which is (-x,0)
paddle_a.goto(-350, 0)

# **Paddle B**
paddle_b = turtle.Turtle()

# Speed of animation set to max possible speed
paddle_b.speed(0)

# Give paddle a built in shape.
# default shape is 20px, 20px
paddle_b.shape("square")

# stretching is multiplying the current size by a factor
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B colour
paddle_b.color("white")

# Turtles draw a line. We don't need that here.
paddle_b.penup()

# The centre of the screen is (0,0)
# Paddle B is on the right hand side which is (+x,0)
paddle_b.goto(350, 0)


# Ball A

ball_a = turtle.Turtle()

# Speed of animation set to max possible speed
ball_a.speed(0)

# Give ball a built in shape.
# default shape is 20px, 20px
ball_a.shape("square")

# Ball A colour
ball_a.color("white")

# Turtles draw a line. We don't need that here.
ball_a.penup()

# The centre of the screen is (0,0)
ball_a.goto(0, 0)
