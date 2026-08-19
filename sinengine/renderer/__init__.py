from sinengine.shapes import Shape, PathShape, ShapeStyle, StyledShape, ShapeGroup


class Renderer:
    def renderShape(self, shape:Shape, style=ShapeStyle()):
        if isinstance(shape, PathShape):
            self.renderPathShape(shape, style)
        elif isinstance(shape, StyledShape):
            self.renderShape(shape.shape, shape.style)
        elif isinstance(shape, ShapeGroup):
            for s in shape.shapes:
                self.renderShape(s, style)

    def renderPathShape(self, shape:PathShape, style=ShapeStyle()):
        raise NotImplementedError