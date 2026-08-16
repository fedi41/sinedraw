import math
import numpy as np

def build_path(
        harmonics,  # [freq, amp, phase]
        resolution: int,
        scale=1,
        origin=(0, 0)
):
    path = []
    step = 1 / resolution

    t = 0
    while t <= 1:
        x, y = 0, 0
        for freq, amp, phase in harmonics:
            angle = 2 * math.pi * freq * t + phase
            x += amp * math.cos(angle)
            y += amp * math.sin(angle)
        path.append((origin[0] + x * scale, origin[1] + y * scale))
        t += step

    return path

def build_path_np(harmonics, resolution: int, scale=1, origin=(0, 0)):
    harmonics = np.array(harmonics)  # shape: (n_harmonics, 3) -> freq, amp, phase
    freq, amp, phase = harmonics[:, 0], harmonics[:, 1], harmonics[:, 2]

    t = np.linspace(0, 1, resolution)

    angles = 2 * np.pi * np.outer(freq, t) + phase[:, None]

    x = np.sum(amp[:, None] * np.cos(angles), axis=0)
    y = np.sum(amp[:, None] * np.sin(angles), axis=0)

    x = origin[0] + x * scale
    y = origin[1] + y * scale

    return np.stack([x, y], axis=1)