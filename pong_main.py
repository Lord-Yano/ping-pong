# Ping pong game using turtle module
import turtle

# create a window
wn = turtle.Screen()

# give the window a title
wn.title("Pinging Pong by Lord-Yano")

# change window background colour
wn.bgcolor("black")

# change the size of the window
wn.setup(width=800, height=600)

# stop the window from automatically updating. Makes game faster
wn.tracer(0)

# main game loop
while True:
    wn.update
