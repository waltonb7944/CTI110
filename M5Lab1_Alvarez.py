# using turtle graphics to draw a square and triangle
# M5Lab1
# CTI-110
# Brittani Alvarez






def main():


    import turtle

    wn = turtle.Screen()
    pico = turtle.Turtle()
    pico.shape('turtle')

    wn.bgcolor('black')

    pico.color('red')
    pico.pensize(6)

    for i in range(4):
        pico.forward(200)
        pico.right(90)

    pico.left(60)
    pico.forward(200)
    pico.right(120)
    pico.forward(200)


    wn.exitonclick()

main()
