import turtle
screen =turtle.Screen()
screen.bgcolor("lightblue")

square=turtle.Turtle()
side_length=100
for i in range(4):
    square.forward(side_length)
    square.right(90)
turtle.done()    