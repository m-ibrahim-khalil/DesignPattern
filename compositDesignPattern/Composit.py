import turtle
from tkinter import *

class Ishape():
    def draw(self):
        pass


class Gui:
    def drawing(self,x):
        if (x == 3):
            t = turtle.Turtle()
            for i in range(x):
                t.forward(100)
                t.left(120)
            turtle.done()
        if (x == 4):
            t = turtle.Turtle()
            for i in range(x):
                t.forward(100)
                t.left(90)
            turtle.done()

        if (x == 5):
            t = turtle.Turtle()
            t.forward(200)
            t.left(90)
            t.forward(120)
            t.left(90)
            t.forward(200)
            t.left(90)
            t.forward(120)
            t.left(90)
            t.forward(100)
            t.circle(60)
            turtle.done()


class Line(Ishape):
    def __init__(self):
        self.shape = "Line"

    def draw(self):
        t = turtle.Turtle()
        t.forward(100)
        turtle.done()




class Circle(Ishape):
    def __init__(self):
        self.shape = "Circle"

    def draw(self):
        t = turtle.Turtle()
        t.circle(50)
        turtle.done()

class Composite(Ishape):
    shape = []
    def draw(self):
        self.buildShape()
        count = 0
        y = 0
        for i in self.shape:
            if (i.shape == "Line"):
                count += 1
            elif(i.shape == "Circle"):
                count += 1
            elif(i.Shape == 'Rectangle'):
                count += 4
        Gui().drawing(count)

    def buildShape(self):
        pass


class Flag(Composite):
    def buildShape(self):
        self.shape = []
        self.shape.append(Rectangle())
        self.shape.append(Circle())


class Rectangle(Composite):
    Shape = "Rectangle"
    def buildShape(self):
        self.shape = []
        for i in range (4):
            self.shape.append(Line())


class Triangle(Composite):
    def buildShape(self):
        for i in range(3):
            self.shape.append(Line())


class Client():
    def draw_line(self):
        Line().draw()

    def draw_flag(self):
        Flag().draw()

    def draw_circle(self):
        Circle().draw()

    def draw_triangle(self):
        Triangle().draw()

    def draw_rectangle(self):
        Rectangle().draw()

if __name__ == '__main__':
    client = Client()
    app = Tk()
    app.title('Composit DP')
    app.geometry('700x350')
    lineButton = Button(app,text ='Draw line',width = 12, command = client.draw_line)
    lineButton.grid(row = 3,column = 0, pady=20)
    lineButton = Button(app, text='Draw Circle', width=12, command = client.draw_circle)
    lineButton.grid(row=4, column=0, pady=20)
    lineButton = Button(app, text='Draw Triangle', width=12, command = client.draw_triangle)
    lineButton.grid(row=5, column=0, pady=20)
    lineButton = Button(app,text ='Draw Rectangle',width = 12, command = client.draw_rectangle)
    lineButton.grid(row = 6,column = 0, pady=20)
    lineButton = Button(app,text ='Draw flag',width = 12, command = client.draw_flag)
    lineButton.grid(row = 8,column = 0, pady = 20)

    app.mainloop()

