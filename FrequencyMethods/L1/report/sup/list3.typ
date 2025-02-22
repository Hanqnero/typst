```py
from fourier import *
import numpy as np
import matplotlib.pyplot as plt

T = 8
R = 2
def func(xs: np.array):
    global T, R
    xs = (xs+T/8)%T-T/8
    real = np.piecewise(xs,
        [
           np.logical_and(  -T/8 <= xs , xs < T/8), 
           np.logical_and(   T/8 <= xs , xs < 3*T/8),
           np.logical_and( 3*T/8 <= xs , xs < 5*T/8),
           np.logical_and( 5*T/8 <= xs , xs < 7*T/8),
         ],
         [
             lambda _: R,
             lambda xs: 2*R-8*R*xs/T,
             lambda _: -R,
             lambda xs: -6*R+8*R*xs/T
         ]
    )
    imag = np.piecewise(xs,
        [
           np.logical_and(  -T/8 <= xs , xs < T/8), 
           np.logical_and(   T/8 <= xs , xs < 3*T/8),
           np.logical_and( 3*T/8 <= xs , xs < 5*T/8),
           np.logical_and( 5*T/8 <= xs , xs < 7*T/8),
         ],
         [
             lambda xs: (8*R*xs/T),
             lambda _: (R),
             lambda xs: (4*R-8*R*xs/T),
             lambda _: (-R)
         ]
    )
    return real + 1j*imag

xs = np.linspace(-2*T, 2*T, 1000)
ys0 = func(xs)
ys = ys0

fig, ax = plt.subplots(ncols=2, sharey=True)
fig.set_size_inches(10, 3)

ax[0].set_ylabel("$Re(f(t))$")
ax[1].set_ylabel("$Im(f(t))$")
ax[0].set_xlabel("$t$")
ax[1].set_xlabel("$t$")

ax[0].plot(xs, np.real(ys))
ax[1].plot(xs, np.imag(ys))

fig.savefig("fig/comp/f.svg", format='svg', bbox_inches='tight')

for N in [1, 2, 3, 10]:
    ys = G_N_sum(func, T, N)(xs)
    re = np.real(ys)
    im = np.imag(ys)

    ax[0].clear(); ax[1].clear();
    ax[0].set_ylabel("$Re(f(t))$")
    ax[1].set_ylabel("$Im(f(t))$")
    ax[0].set_xlabel("$t$")
    ax[1].set_xlabel("$t$")


    ax[0].plot(xs, np.real(ys0))
    ax[0].plot(xs, re)

    ax[1].plot(xs, np.imag(ys0))
    ax[1].plot(xs, im)
    fig.savefig(f'fig/comp/N{N}.svg', format='svg', bbox_inches='tight')

# Значение коэффициентов c_n
np.set_printoptions(precision=5, linewidth=120)
print(np.array(list(G_N(func, T, 2))))

# Проверка равенства Парсеваля
xs = np.linspace(-T/2, T/2, 2000)
ys = func(xs)

lhs = np.abs(np.trapezoid(ys*np.conj(ys), xs))
rhs = 0
for _, c_, omega in (G_N(func, T, 50, 2000)):
    rhs += abs(c_)**2 * abs(np.trapezoid( np.exp(-1j * omega * xs) * np.exp(1j * omega * xs), xs))

print(lhs, rhs)

print((rhs - lhs)/lhs*100)```
