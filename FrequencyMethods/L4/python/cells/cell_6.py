# фильтрация через произведение перед. функции на образ
def apply_W_nondynamic(t, signal, W, dt=None):
    if dt is None:
        dt = t[1] - t[0]

    fr = np.fft.fftfreq(signal.size, dt)
    fft = np.fft.fft(signal)

    return np.real(np.fft.ifft( W_poly(W)(1j*2*np.pi*fr)*fft ))

# честная динамическая фильтрация дискретного сигнала
def apply_W_dynamic(t, signal, W, dt=None):
    if dt is None:
        dt = t[1] - t[0]

    b, a = sp.signal.bilinear(W[0], W[1], 1/dt)
    y_out = sp.signal.lfilter(b, a, signal)

    return y_out

