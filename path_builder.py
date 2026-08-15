import math

def build_path(
        harmonics:list[list[int]],
        resolution:int, scale=1, origin=(0,0)
):
    path = []

    t = 0
    while t <= 1:
        x,y = 0,0
        for harmonic in harmonics:
            x+=math.sin(harmonic[0]+harmonic[2]+t)*harmonic[1]
            y+=math.sin(harmonic[0]+harmonic[2]+t)*harmonic[1]
        t += 0.1
        path.append((origin[0]+x*scale,origin[1]+y*scale))

    return path



