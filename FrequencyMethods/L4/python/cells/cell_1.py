import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import scipy as sp
def figsize(width, ratio):
    width /= 25.4
    height = width / ratio
    return (width, height)

fig16by9 = figsize(200, 16/9)

plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = ['Times New Roman', 'Helvetica', 'serif']

plt.rcParams['font.size'] = 11
plt.rcParams['figure.figsize'] = fig16by9
plt.rcParams['figure.dpi'] = 350

plt.rcParams['lines.linewidth'] = .9