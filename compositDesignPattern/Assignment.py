import turtle
import tkinter as tk
from abc import ABC

SPEED = 5
BG_COLOR = "#6200EE"
BBG_COLOR = "#6495ed"
BFG_COLOR = "white"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "Drawing Board"


class IShape(ABC):
    def draw(self):
        pass

    def build(self):
        pass


class CompositeShape(IShape, ABC):
    def __init__(self):
        self.shapes = []

    def build(self):
        pass

    def draw(self):
        self.build()
        for shape in self.shapes:
            shape.draw()


class Line(IShape):
    def __init__(self, artist, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.artist = artist

    def draw(self):
        self.artist.penup()
        self.artist.goto(self.x1, self.y1)
        self.artist.pendown()
        self.artist.goto(self.x2, self.y2)

    def build(self):
        print('draw a line')


class Circle(IShape):
    def __init__(self, artist, r):
        self.artist = artist
        self.r = r
        self.artist.color('red')
        self.artist.fillcolor('red')

    def draw(self):
        self.artist.penup()
        self.artist.sety(-self.r)
        self.artist.setx(0)
        self.artist.pendown()
        self.artist.begin_fill()
        self.artist.circle(self.r)
        self.artist.end_fill()

    def build(self):
        print('pie')


class Triangle(CompositeShape):
    def __init__(self, artist):
        CompositeShape.__init__(self)
        self.artist = artist
        self.artist.color('black')

    def build(self):
        self.shapes.append(Line(self.artist, -150, 0, 150, 0))
        self.shapes.append(Line(self.artist, 150, 0, 0, 200))
        self.shapes.append(Line(self.artist, 0, 200, -150, 0))


class Rectangle(CompositeShape):
    def __init__(self, artist):
        CompositeShape.__init__(self)
        self.artist = artist
        self.artist.color(PEN_COLOR)

    def build(self):
        self.shapes.append(Line(self.artist, -100, -75, 100, -75))
        self.shapes.append(Line(self.artist, 100, -75, 100, 75))
        self.shapes.append(Line(self.artist, 100, 75, -100, 75))
        self.shapes.append(Line(self.artist, -100, 75, -100, -75))


class Flag(CompositeShape):
    def __init__(self, artist):
        CompositeShape.__init__(self)
        self.artist = artist
        self.rectangle = Rectangle(self.artist)
        self.circle = Circle(self.artist, 50)

    def build(self):
        self.shapes.append(self.rectangle)
        self.shapes.append(self.circle)


class Star(CompositeShape):
    def __init__(self, artist):
        CompositeShape.__init__(self)
        self.artist = artist
        self.artist.color('yellow')

    def build(self):
        self.shapes.append(Line(self.artist, 60, 20, 20, 110))
        self.shapes.append(Line(self.artist, 20, 110, 110, 50))
        self.shapes.append(Line(self.artist, 110, 50, 10, 50))
        self.shapes.append(Line(self.artist, 10, 50, 100, 110))
        self.shapes.append(Line(self.artist, 100, 110, 60, 20))


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing app by composite pattern")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=400)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor(BG_COLOR)

        self.button = tk.Button(self.master, text="Draw line", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_line)
        self.button.pack(padx=6, pady=(50, 2))

        self.button = tk.Button(self.master, text="Draw Circle", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_circle)
        self.button.pack(padx=6, pady=4)

        self.button = tk.Button(self.master, text="Draw Triangle", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_triangle)
        self.button.pack(padx=6, pady=4)

        self.button = tk.Button(self.master, text="Draw Rectangle", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_rectangle)
        self.button.pack(padx=6, pady=4)

        self.button = tk.Button(self.master, text="Draw Flag", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_flag)
        self.button.pack(padx=6, pady=4)

        self.button = tk.Button(self.master, text="Draw Star", width=12, bg=BBG_COLOR, fg=BFG_COLOR, command=self.draw_star)
        self.button.pack(padx=6, pady=4)

        self.artist = turtle.RawTurtle(self.screen)
        self.artist.hideturtle()
        self.artist.pensize(PEN_WIDTH)
        self.artist.color(PEN_COLOR)
        self.artist.speed(SPEED)

    def draw_line(self):
        self.artist.clear()
        line = Line(self.artist, -50, 100, 100, -50)
        line.draw()

    def draw_flag(self):
        self.artist.clear()
        Flag(self.artist).draw()

    def draw_circle(self):
        self.artist.clear()
        Circle(self.artist, 100).draw()

    def draw_triangle(self):
        self.artist.clear()
        Triangle(self.artist).draw()

    def draw_rectangle(self):
        self.artist.clear()
        Rectangle(self.artist).draw()

    def draw_star(self):
        self.artist.clear()
        Star(self.artist).draw()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()