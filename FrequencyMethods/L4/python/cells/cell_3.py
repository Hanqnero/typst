N = 2**10 * 4
t = np.linspace(0.5, 4.5, N)
signal = noisy_signal(t, 1, 0, 1)
clean_signal = g(t)