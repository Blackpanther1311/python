import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(500,400)
star = turtle.Turtle()

#firsttriangle forstar
star.forward(100)

star.left(120)
star.forward(100)

star.left(120)
star.forward(100)

star.penup()
star.right(150)
star.forward(50)
star.pendown()

#second triangle for star
star.right(90)
star.forward(100)

star.right(120)
star.forward(100)

star.right(120)
star.forward(100)

turtle.done()