from sinengine.shapes import Shape, ShapeStyle


class Sprite:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes:list[Shape] = shapes





