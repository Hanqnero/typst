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

    ax.plot(t, clean_signal,  'k--', alpha=.9, label='исходный сигнал')
    ax.plot(t, _noisy_signal,  'r-', alpha=.5, label='зашумленный сигнал')
    ax.plot(t, out_signal, 'g-', alpha=.8, label='фильтрованный сигнал')

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

    fr = np.fft.fftfreq(t.size, t[1] - t[0])[0:t.size//2]
    noisy_fft = np.abs(np.fft.fft(_noisy_signal)[0:t.size//2]) / t.size

    filtered_fr = np.fft.fftfreq(t.size, t[1] - t[0])[0:t.size//2]
    filtered_signal = np.abs((np.fft.fft(out_signal))[0:t.size//2]) / t.size

    plt.plot(fr, noisy_fft)
    plt.plot(filtered_fr, filtered_signal)

    plt.savefig(f"../fig/1/2/d/{2*i+1}.png")