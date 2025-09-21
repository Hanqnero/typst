import os
import functools
import time

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from numpy.fft import fft, ifft, fftshift, ifftshift, fftfreq

TAU = np.pi * 2


def rect(t):
    return np.where(np.abs(t) <= 0.5, 1, 0)


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {(end_time - start_time)*1000:.4f} ms")
        return result

    return wrapper


def trapz_ft(signal, t, v):
    dt = t[1] - t[0]
    y = signal * np.exp(-1j * TAU * v[..., np.newaxis] * t)
    integral = np.trapezoid(y, dx=dt, axis=1)

    assert integral.shape == v.shape
    return integral


@timeit
def perform_ft(signal, t):
    v = fftshift(fftfreq(t.size, t[1] - t[0]))
    _ = trapz_ft(signal, t, v)


@timeit
def perform_fft(signal, t):
    _ = fftshift(fft(signal, norm="ortho"))


for T, dt in (
    (5, 0.005),
    (10, 0.005),
    (5, 0.0005),
):
    t = np.arange(-T / 2, T / 2, dt)
    print(f"N = {t.size}")
    signal = rect(t)
    perform_ft(signal, t)
    perform_fft(signal, t)
