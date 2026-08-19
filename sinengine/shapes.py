import numpy as np


from sinengine.path_builder import build_path
from sinengine.util import align_harmonics, lerp_harmonics, points_to_harmonics



# ---------- styles

class ShapeStyle:
    def __init__(self, color="#ffffff", width=2, resolution=200, scale=1, offset=(0,0), transform=lambda harmonics : harmonics):
        self.color = color
        self.width = width
        self.resolution = resolution
        self.scale = scale
        self.offset = offset
        self.transform = transform


# ---------- basic shape classes
class Shape: pass

class PathShape(Shape):
    def build_path(self, resolution=200, scale=1, offset=(0, 0), transform=lambda harmonics : harmonics):
        raise NotImplementedError

# ---------- path shapes
class HarmonicShape(PathShape):
    def __init__(self, harmonics = []):
        if  len(harmonics)==0:
            harmonics = [[0,0,0]]
        self.harmonics = np.array(harmonics)  # [freq, amp, phase]

    @classmethod
    def from_points(cls, points):
        return cls(points_to_harmonics(points))

    def top_n(self, n):
        idx = np.argsort(-self.harmonics[:, 1])
        return HarmonicShape(self.harmonics[idx[:n]])

    def build_path(self, resolution=200, scale=1, offset=(0, 0), transform=lambda harmonics : harmonics):
        return build_path(transform(self.harmonics), resolution, scale, offset)

class MorphShape(PathShape):
    def __init__(self, harmonics1, harmonics2):
        self.harmonics1, self.harmonics2 = align_harmonics(harmonics1, harmonics2)
        self.progress = 0

        self._morphed_harmonics = lerp_harmonics(self.harmonics1, self.harmonics2, self.progress)

    def set_progress(self, progress):
        self.progress = progress
        self._morphed_harmonics = lerp_harmonics(self.harmonics1, self.harmonics2, self.progress)

    def build_path(self, resolution=200, scale=1, offset=(0, 0), transform=lambda harmonics : harmonics):
        return build_path(transform(self._morphed_harmonics), resolution, scale, offset)

# ---------- Special shapes
class ShapeGroup(Shape):
    def __init__(self, shapes=None):
        self.shapes = shapes or []

    def add(self, shape:Shape):
        self.shapes.append(shape)
class StyledShape(Shape):
    def __init__(self, shape=Shape(), style=ShapeStyle()):
        self.shape = shape
        self.style = style


