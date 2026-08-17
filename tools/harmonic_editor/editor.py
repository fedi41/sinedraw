import numpy as np
import pygame

from core.harmonics import harmonics_star, HarmonicSprite, HarmonicShape, RenderStyle
from renderer.pygame_renderer import PygameRenderer
from tools.harmonic_editor.preview import PreviewSprite

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
        self.preview_sprite = PreviewSprite()

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
            if not self.mouse_was_pressed:
                print(self.preview_sprite.shapes[-1].shape.harmonics)
                self.preview_sprite.new_shape()
                self.raw_points = []
            self.mouse_was_pressed = True

            self.raw_points.append((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            self.preview_sprite.modify_last_shape(np.array(self.raw_points)-self.origin, 15)
            # print(self.preview_sprite.shapes.harmonics)
        else:
            self.mouse_was_pressed = False

    def render(self):
        self.screen.fill("#0F1A20")

        # print(self.test_sprite.render(200, 100,self.origin))
        self.renderer.draw(self.preview_sprite, 100, 1,self.origin)

        self.renderer.draw_lines("yellow", np.array(self.raw_points), 1)

        pygame.draw.circle(self.screen, "green", self.origin, 1)




if __name__ == '__main__':

    window = MainWindow()
    window.run()


