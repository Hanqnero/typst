def g_(a, t1, t2):
    return lambda t: np.piecewise(t,
    [t > t2, t <= t2, t < t1],
    [0, a, 0]                    
    )

g = g_(1, 2, 3)

def xi(t):
    return np.random.uniform(-1, 1, size=t.size)

def wave(t, d):
    return np.sin(d*t)

def noisy_signal(t, b, c, d):
    return g(t) + b*xi(t) + c*wave(t, d)