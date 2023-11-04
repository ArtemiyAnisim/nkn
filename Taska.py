class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print(f'рисуем фигуру цветом {self.color} и шириной {self.width}')


class Line(Figure):
    pass

class Rect(Figure):

    def __init__(self, coords, width, color, right):
        super(Rect, self).__init__(coords, width, color)
        self.right = right

        def draw(self):
            print(f'рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')


f = Figure([1, 2, 4, 5, 7, 8], 2, 'black')
f.draw()

l = Line([1, 1, 5, 6], 3, 'red')
l.draw()
