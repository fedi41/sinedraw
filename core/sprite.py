from core.shapes import Shape, RenderStyle


class Sprite:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes:list[Shape] = shapes





