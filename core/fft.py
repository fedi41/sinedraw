import numpy as np


#
def points_to_harmonics(points):
    points = np.array(points)
    x,y = points[:,0],points[:,1]

    z = x + 1j * y # complex

    n = len(z)
    coeffs = np.fft.fft(z)/n

    freqs = np.fft.fftfreq(n, d=1/n)

    amp = np.abs(coeffs)
    phase = np.angle(coeffs)

    harmonics = np.stack([freqs, amp, phase], axis=1)
    return harmonics