import pygame

from core.harmonics import HarmonicSprite


class PygameRenderer:
    def __init__(self, surface):
        self.surface = surface

    def draw(self, sprite:HarmonicSprite, resolution=200, scale=1, origin=(400, 300)):
        for points, style in sprite.render(resolution=resolution, scale=scale, origin=origin):
            color = pygame.Color(style.color)
            point_list = [(float(x), float(y)) for x, y in points]

            self.draw_lines(color, point_list, style.width)
            self.draw_points(color, point_list, style.width)

    def draw_lines(self, color, points, width):
        if len(points) >= 2:
            pygame.draw.lines(self.surface, color, True, points, width)

    def draw_points(self, color, points, radius):
        for p in points:
            pygame.draw.circle(self.surface, color, p, radius)