
def check_roots(b, c):
    D = np.complex128(b**2 - 4*c)
    roots = np.real((-b + np.sqrt(D))/2), np.real((-b - np.sqrt(D))/2)
    return all(map(lambda x: x < 0, roots)), roots

def W2_tf(a1, a2, b1, b2):
    assert check_roots(b1, b2), "Фильтр неустойчивый"

    return W_tf([1, a1, a2], [1, b1, b2])

def W2(a1, a2, b1, b2):
    roots = check_roots(b1, b2)
    assert roots[0], ("Фильтр неустойчивый", roots[1])

    return lambda p: (p**2 + a1*p + a2)/(p**2 + b1*p + b2)
