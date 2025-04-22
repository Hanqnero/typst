W_tf = lambda num, den: (num, den)
W1_tf = lambda T: W_tf([1], [T, 1])

# передаточная функция от произвольного аргумента
def W_poly(W):
    return lambda p: sum(p**i*coef for i, coef in enumerate(reversed(W[0]))) / sum(p**i*coef for i, coef in enumerate(reversed(W[1])))