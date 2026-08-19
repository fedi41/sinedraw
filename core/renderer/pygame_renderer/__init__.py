import pygame

from core.renderer import Renderer
from core.shapes import PathShape, ShapeStyle
from core.sprite import Sprite


class PygameRenderer(Renderer):
    def __init__(self, surface):
        self.surface = surface
# TODO
    def renderPathShape(self, shape:PathShape, style=ShapeStyle()):
        path = shape.build_path(style.resolution, style.scale, style.offset)
        self.draw_lines(style.color, path, style.width)

    def draw_lines(self, color, points, width):
        if len(points) >= 2:
            pygame.draw.lines(self.surface, color, True, points, width)

    def draw_points(self, color, points, radius):
        for p in points:
            pygame.draw.circle(self.surface, color, p, radius)



