"""
Drawing graphics using the turtle module
Version: 0.1
Author: slynxes
Date: 2018-12-01
"""
import turtle


def draw_rectangle():
    """
    画矩形
    :return:
    """
    # Set the line thickness to width
    turtle.pensize(4)
    # Set the line color
    turtle.pencolor('green')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    # Starts event loop - calling Tkinter's mainloop function.
    # Must be last statement in a turtle graphics program
    turtle.mainloop()


if __name__ == '__main__':
    draw_rectangle()
