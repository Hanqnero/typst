# фильтрация через произведение перед. функции на образ
def apply_W_nondynamic(t, signal, W, dt=None) -> np.ndarray:
    if dt is None:
        dt = t[1] - t[0]

    fr = np.fft.fftfreq(signal.size, dt)
    fft = np.fft.fft(signal)

    return np.real(np.fft.ifft( W_poly(W)(1j*2*np.pi*fr)*fft ))

# честная динамическая фильтрация дискретного сигнала
def apply_W_dynamic(t, signal, W, dt=None, y0=0) -> np.ndarray:
    if dt is None:
        dt = t[1] - t[0]

    signal -= y0

    tf = sp.signal.TransferFunction(*W)
    t_out, y_out, _ = sp.signal.lsim(tf, U=signal, T=t)

    return y_out + y0
