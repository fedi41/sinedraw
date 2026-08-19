import numpy as np
import pygame

from sinengine.renderer.pygame_renderer import PygameRenderer
from sinengine.shapes import HarmonicShape, ShapeGroup, StyledShape, ShapeStyle

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (1500, 900)


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("sinedraw editor")

        self.origin = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.running = True
        self.renderer = PygameRenderer(self.screen)
        self.t = 0

        self.raw_points = []
        self.shape_group = ShapeGroup()
        self.root_shape = StyledShape(self.shape_group, ShapeStyle(color="red", width=4, resolution=150))
        self.shape_group.add(HarmonicShape())

        self.mouse_was_pressed = False

    def run(self):

        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()

            pygame.display.flip()

    def update(self):

        if pygame.mouse.get_pressed(3)[0]:
            mouse = pygame.mouse.get_pos()
            if not self.mouse_was_pressed:
                print([[float(j) for j in i] for i in self.shape_group.shapes[-1].harmonics])
                self.shape_group.add(HarmonicShape())
                self.raw_points = []
            self.mouse_was_pressed = True
            if not self.raw_points or (mouse[0]-self.raw_points[-1][0])**2 + (mouse[1]-self.raw_points[-1][1])**2 > 10:
                self.raw_points.append((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                self.shape_group.shapes[-1] = HarmonicShape.from_points(np.array(self.raw_points)).top_n(15)
        else:
            self.mouse_was_pressed = False

    def render(self):
        self.screen.fill("#0F1A20")

        self.renderer.renderShape(self.root_shape)

        self.renderer.draw_lines("yellow", np.array(self.raw_points), 1)

        pygame.draw.circle(self.screen, "green", self.origin, 1)




if __name__ == '__main__':

    window = MainWindow()
    window.run()


