import turtle

turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(700,600)
polygon = turtle.Turtle()

num_of_side = 6
angle = 360/num_of_side
length=70

for side in range(num_of_side):
    polygon.forward(length)
    polygon.right(angle)
turtle. done()