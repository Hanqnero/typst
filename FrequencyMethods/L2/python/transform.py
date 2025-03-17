from typing import Callable
import numpy as np


def transform(
        f: Callable[[np.ndarray], np.ndarray], 
        lim: float, 
        n_points=2000) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute the Fourier transform of a function f(t) 
    in the angular velocity domain.
    """
    t = np.linspace(-lim, lim, n_points)
    sr = n_points // lim
    omega = np.linspace(-sr//2, sr//2, n_points)
    f_omega = np.trapezoid(f(t)[np.newaxis,:]*np.exp(-1j*omega[:,np.newaxis]*t), t, axis=1)
    return omega, f_omega/np.sqrt(2*np.pi)
