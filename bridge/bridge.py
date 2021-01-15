
# Circle and square
# vector and raster
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # def render_square(self, side):
    #    pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    # For the open close principle this is not a good solution
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
