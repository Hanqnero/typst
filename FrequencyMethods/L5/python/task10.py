import os
import functools
import time

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from numpy.fft import fft, ifft, fftshift, ifftshift, fftfreq


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {(end_time - start_time)*1000:.4f} ms")
        return result

    return wrapper


plt.rcParams["figure.figsize"] = FIGSIZE = (
    200 / 25.4,
    200 / (16 / 9) / 25.4,
)  # 16 by 9 aspect & 200mm width

FIGSIZE_WIDE = (
    300 / 25.4,
    300 / 2.5 / 25.4,
)  # 5 by 2 aspect & 200mm width


plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams["font.family"] = "serif"
plt.rcParams["figure.dpi"] = 300

PI = np.pi
TAU = 2 * np.pi


def add_grid(ax: Axes):
    ax.grid(which="major", linestyle="-", alpha=0.6)
    ax.grid(which="minor", linestyle=":", alpha=0.4)


T = 5
dt = 0.005
t = np.arange(-T / 2, T / 2, dt)

Pi = np.piecewise(
    t,
    [
        t > 1 / 2,
        t <= 1 / 2,
        t < -1 / 2,
    ],
    [0, 1, 0],
)

V = 50
dv = 0.005
v = np.arange(-V / 2, V / 2, dv)

Pi_hat = np.sinc(v)

os.makedirs("../fig/task1/1.0", exist_ok=True)

plt.figure()
plt.plot(t, Pi, "-", color="grey")
add_grid(plt.gca())
plt.xlim(-T / 2, T / 2)
plt.xlabel("$t$")
plt.ylabel(r"$\Pi(t)$")
plt.savefig("../fig/task1/1.0/f.png")
plt.close()

plt.figure()
plt.plot(v, Pi_hat, "-", color="grey")
add_grid(plt.gca())
plt.xlabel(r"$\nu$")
plt.ylabel(r"$\hat{\Pi}(t)$")
plt.xlim(-V / 2, V / 2)
plt.savefig("../fig/task1/1.0/F_hat.png")
plt.close()
