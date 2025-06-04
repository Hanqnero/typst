%mkdir -p ../fig/1/2/d

# См.:
# https://en.wikipedia.org/wiki/Band-stop_filter

omega0 = 2*np.pi * 20

a1 = 0
a2 = omega0**2
b1 = 10**3
b2 = omega0**2

_W = W2_tf(a1, a2, b1, b2)


for i, _f0 in enumerate((25, 40, 60)):

    _wave = wave(t, 2*np.pi*_f0)
    _noisy_signal = clean_signal + _wave

    # -----------------------------------------------
    # Cравнение зашумленного и фильтрованного сигнала
    # -----------------------------------------------
    plt.figure(num=2*i)
    ax = plt.gca()

    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
    ax.grid(which='major', linestyle='--', alpha=0.6)
    ax.grid(which='minor', linestyle=':', alpha=0.3)

    out_signal = apply_W_dynamic(t, _noisy_signal, _W)
    out_signal2 = apply_W_nondynamic(t, _noisy_signal, _W)

    ax.plot(t, clean_signal,  'k--', alpha=.9, label='исходный сигнал')
    ax.plot(t, _noisy_signal,  'r-', alpha=.5, label='зашумленный сигнал')
    ax.plot(t, out_signal, 'g-', alpha=.8, label='фильтрованный сигнал')
    ax.plot(t, out_signal2, 'b:', alpha=.7, label="$\\mathcal{F}^{-1}\\{W_{2}(i \\omega)\\mathcal{F}u(t)\\}$")

    ax.text(0.85, 0.90, f"$b=0$\n$c=1$\n$d=2\\pi\\times{_f0}$", transform=ax.transAxes, 
             verticalalignment='top', horizontalalignment='left',
             bbox=dict(facecolor='white', alpha=0.8))

    plt.legend()
    plt.savefig(f"../fig/1/2/d/{2*i}.png")

    # -----------------------------------------------
    # Cравнение зашумленного и фильтрованного образа
    # -----------------------------------------------
    plt.figure(num=2*i+1)
    ax = plt.gca()

    ax.set_xlim(right=100)

    
    freqs = np.fft.fftfreq(t.size, t[1] - t[0])[0:t.size//2]
    noisy_fft = np.abs(np.fft.fft(_noisy_signal)[0:t.size//2]) / t.size
    clean_fft = np.abs(np.fft.fft(clean_signal)[0:t.size//2]) / t.size

    filtered_fft_dyn = np.abs((np.fft.fft(out_signal))[0:t.size//2]) / t.size
    filtered_fft_nondyn = np.abs((np.fft.fft(out_signal2))[0:t.size//2]) / t.size

    plt.plot(freqs, clean_fft, 'k--', alpha=.7, label='исходный сигнал')
    plt.plot(freqs, noisy_fft, 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(freqs, filtered_fft_dyn, 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(freqs, filtered_fft_nondyn, 'b:', alpha=.7, label="$W_{2}(i \\omega)\\mathcal{F}u(t)$")

    plt.grid(which='major', linestyle=':', alpha=0.6)

    plt.legend()

    plt.savefig(f"../fig/1/2/d/{2*i+1}.png")