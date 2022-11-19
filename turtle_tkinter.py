import turtle
from tkinter import *

def color():
    my_turtle.fillcolor('cyan')
    my_turtle.begin_fill()
    my_turtle.end_fill()

def stairs():
    for i in range(7):
        my_turtle.pencolor('blue')
        my_turtle.forward(30)
        my_turtle.right(90)
        my_turtle.pencolor('blue')
        my_turtle.forward(30)
        my_turtle.left(90)
        
def square():
    for i in range(4):
        my_turtle.pencolor('yellow') 
        my_turtle.forward(200)
        my_turtle.right(90)
                
def triangle():
    for i in range(3):
        my_turtle.pencolor('cyan')       
        my_turtle.forward(200)
        my_turtle.left(120)
                       
def star():
    my_turtle.pencolor('blue')
    for i in range(5):
        my_turtle.forward(100)
        my_turtle.right(144)
                
def clear():
        my_turtle.clear()

def reset():
        my_turtle.reset()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("pink")
    canvas = screen.getcanvas()
    button = Button(canvas.master, text="Stairs", command=stairs, bg='blue', fg='white').pack(side=LEFT)
    button2 = Button(canvas.master, text="Square", command=square, bg='yellow').pack(side=LEFT)
    button3 = Button(canvas.master, text="Triangle", command=triangle, bg='cyan', fg='white').pack(side=LEFT)
    button4 = Button(canvas.master, text="Star", command=star, bg='blue', fg='white').pack(side=LEFT)
    button5 = Button(canvas.master, text="Crear", command=clear).pack(side=RIGHT)
    button6 = Button(canvas.master, text="Reset", command=reset).pack(side=RIGHT)
    canvas.create_window(-395, -350, window=button)
    canvas.create_window(-350, -350, window=button2)
    canvas.create_window(-300, -350, window=button3)
    canvas.create_window(-300, -350, window=button4)

    my_turtle = turtle.Turtle(shape="turtle")
    turtle.done()
    



