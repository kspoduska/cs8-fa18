import turtle

def bullseye():
    # Bullseye
    turtle.dot(100, 'red')
    turtle.dot(80, 'black')
    turtle.dot(60, 'red')
    turtle.dot(40, 'black')
    turtle.dot(20, 'red')

def cube():
    # Base square
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    turtle.left(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)

    turtle.right(135)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)

def hexagon():
    # Hexagon
    for _ in range(6):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.left(60)
    
bullseye()
turtle.up()
turtle.setx(100)
turtle.down()
cube()
turtle.up()
turtle.setx(-50)
turtle.sety(-200)
turtle.down()
hexagon()    
