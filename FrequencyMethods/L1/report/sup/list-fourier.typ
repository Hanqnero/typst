```py
import numpy as np

def F_N(func, T, N, n_points=2000):
    """
    Generator that yields tuples of `(n, a_n, b_n, omega_n)`

    for `n = 0` yields `(0, a_0, a_0, 0)`
    """
    xs = np.linspace(-T/2,T/2, n_points)
    ys = np.vectorize(func)(xs)
    a0 = 1/T * np.trapezoid(ys, xs)
    yield (0, a0, a0, 0)

    for n in range(1, N+1):
        omega = 2*np.pi * n / T 
        a = 2/T * np.trapezoid(ys * np.cos(omega * xs), xs)
        b = 2/T * np.trapezoid(ys * np.sin(omega * xs), xs)
        yield (n, a, b, omega)
    return

def G_N(func, T, N ,n_points=2000):
    """
    Generator that yields tuples of `(n, c_n, omega_n)`
    """
    xs = np.linspace(-T/2,T/2, n_points)
    ys = np.vectorize(func)(xs)
    for n in range(-N, N+1):
        omega = 2*np.pi * n / T 
        c = 1/T * np.trapezoid(ys * np.exp(-1j*omega*xs), xs)
        yield (n, c, omega)
    return

def G_N_sum(func, T, N, n_points=2000):
    """Returns partial sum `G_N(t)`"""
    gen = G_N(func, T, N, n_points)
    other = np.array(list(gen))
    c = other[:, 1]; omega = other[:, 2]
    return lambda t: np.sum(
            c[:,np.newaxis]*np.exp(1j * omega[:,np.newaxis]*t), axis=0)


def F_N_sum(func, T, N, n_points=2000):
    """Returns partial sum `F_N(t)`"""
    gen = F_N(func, T, N, n_points)
    a0 = next(gen)[1]
    other = np.array(list(gen))
    a = other[:, 1]; b = other[:, 2]; omega = other[:, 3]
    return lambda t: a0 + np.sum(
                a[:,np.newaxis]*np.cos(omega[:,np.newaxis]*t) +
                b[:,np.newaxis]*np.sin(omega[:,np.newaxis]*t), axis=0)
```
