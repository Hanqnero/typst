%mkdir -p ../fig/1/2/b1

for i, _b1 in enumerate((50, 10**2, 3*10**2)):
    # -----------------------------------------------
    # АЧХ Фильтра
    # -----------------------------------------------
    plt.figure(num=3*i)
    ax = plt.gca()

    ax.xaxis.set_major_locator(plt.MultipleLocator(100))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(20))
    ax.grid(which='major', linestyle='--', alpha=0.6)
    ax.grid(which='minor', linestyle=':', alpha=0.3)

    ax.set_ylim(top=1.1)

    # См.:
    # https://en.wikipedia.org/wiki/Band-stop_filter

    omega0 = 2*np.pi * 20

    a1 = 0
    a2 = omega0**2
    b1 = _b1
    b2 = omega0**2

    _W = W2_tf(a1, a2, b1, b2)

    ax.text(0.75, 0.15, f"$b_1 = {b1}$\n$\\omega_{0}=2\\pi\\times20$", transform=ax.transAxes, 
             verticalalignment='top', horizontalalignment='left',
             bbox=dict(facecolor='white', alpha=0.8))

    plot_freq_response(_W, ax, t)

    plt.savefig(f"../fig/1/2/b1/{3*i}.png")

    # -----------------------------------------------
    # Cравнение зашумленного и фильтрованного сигнала
    # -----------------------------------------------
    plt.figure(num=3*i+1)
    ax = plt.gca()

    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
    ax.grid(which='major', linestyle='--', alpha=0.6)
    ax.grid(which='minor', linestyle=':', alpha=0.3)

    out_signal = apply_W_dynamic(t, noisy_signal1, _W)
    out_signal2 = apply_W_nondynamic(t, noisy_signal1, _W)

    ax.plot(t, noisy_signal1, 'r-', alpha=.5, label='зашумленный сигнал')
    ax.plot(t, out_signal, 'g-', alpha=.5, label='фильтрованный сигнал')
    ax.plot(t, out_signal2, 'b:', alpha=.7, label="$\\mathcal{F}^{-1}\\{W_{2}(i \\omega)\\mathcal{F}u(t)\\}$")

    ax.text(0.75, 0.90, f"$b=0$\n$c=1$\n$d=2\\pi\\times20$", transform=ax.transAxes, 
             verticalalignment='top', horizontalalignment='left',
             bbox=dict(facecolor='white', alpha=0.8))
    
    ax.legend()

    plt.savefig(f"../fig/1/2/b1/{3*i+1}.png")

    # -----------------------------------------------
    # Cравнение зашумленного и фильтрованного образа
    # -----------------------------------------------
    plt.figure(num=3*i+2)
    ax = plt.gca()

    ax.set_xlim(right=100)

    freqs = np.fft.fftfreq(t.size, t[1] - t[0])[0:t.size//2]

    noisy_fft = np.abs(np.fft.fft(noisy_signal1)[0:t.size//2]) / t.size

    filtered_fft_dyn = np.abs((np.fft.fft(out_signal))[0:t.size//2]) / t.size
    filtered_fft_nondyn = np.abs((np.fft.fft(out_signal2))[0:t.size//2]) / t.size

    plt.plot(freqs, noisy_fft, 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(freqs, filtered_fft_dyn, 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(freqs, filtered_fft_nondyn, 'b:', alpha=.7, label="$W_{2}(i \\omega)\\mathcal{F}u(t)$")


    plt.grid(which='major', linestyle=':', alpha=0.6)

    plt.legend()

    plt.savefig(f"../fig/1/2/b1/{3*i+2}.png")