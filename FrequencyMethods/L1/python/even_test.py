import numpy as np
import matplotlib.pyplot as plt
from fourier import *


func = lambda x: np.cos(2*x)*np.sin(3*x)*np.sin(x)
T = np.pi

xs = np.linspace(-2*np.pi, 2*np.pi, 2000)

for N in [2,3,4,27,50]:
    fs_func = F_N_sum(func, T, N)
    fs_func_comp = G_N_sum(func, T, N)

    fig, ax = plt.subplots()
    ax.set_xlabel("$t$")
    ax.set_ylabel("$F_N (t)$")
    ax.grid(True)

    ax.plot(xs, func(xs))
    ax.plot(xs, fs_func(xs))
    fig.savefig(f'../fig/even/N{N}.svg', format='svg', bbox_inches='tight')

    fig, ax = plt.subplots(clear=True)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$G_N (t)$")
    ax.grid(True)

    ax.plot(xs, func(xs))
    ax.plot(xs, fs_func_comp(xs))
    fig.savefig(f'../fig/even/N{N}-comp.svg', format='svg', bbox_inches='tight')

F = list(F_N(func, T, 50))
G = list(G_N(func, T, 50))

xs = np.linspace(-T/2, T/2, 2000)

s = np.trapezoid(func(xs)**2, xs)

s1 = 0
for _, a_, b_, omega_ in F:
    s1 += a_**2 * np.trapezoid(np.cos(omega_*xs)**2, xs)
    s1 += b_**2 * np.trapezoid(np.sin(omega_*xs)**2, xs)

s2 = 0
for n_, c_, omega in G:
    s2 += abs(c_)**2 * abs(np.trapezoid( np.exp(-1j * omega * xs) * np.exp(1j * omega * xs), xs))

print(s, s1, s2)
print((s2 - s)/s*100)

F = list(F_N(func, T, 2))
G = list(G_N(func, T, 2))

print(F[:3])
print(G[:3])
