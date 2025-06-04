%mkdir -p ../fig/1/1/a/func
%mkdir -p ../fig/1/1/a/conv

noise = xi(t)
w = W1_tf(.01)

for i, a in enumerate((1,2,3), start=3):

    # =======================
    # Сравненение результатов
    # =======================

    plt.figure()

    clean_signal1 = g_(a, 2, 3)(t)
    noisy_signal1 = clean_signal1 + noise

    filtered_fft_dyn = apply_W_dynamic(t, noisy_signal1, w)
    out2 = apply_W_nondynamic(t, noisy_signal1, w)

    plt.plot(t, noisy_signal1, 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(t, filtered_fft_dyn, 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(t, out2, 'b:', alpha=.4, label="$\\mathcal{F}^{-1}\\{W_{1}(i \\omega)\\mathcal{F}u(t)\\}$")
    plt.plot(t, clean_signal1, 'k--', alpha=.6, label='исходный сигнал')
    plt.legend()


    plt.grid(which='major', linestyle=':', alpha=0.6)
    plt.xlabel('$t$')

    plt.savefig(f"../fig/1/1/a/func/{i}.png")

    # ======
    # Образы
    # ======

    plt.figure()

    _clean_signal = clean_signal1
    _noisy_signal = noisy_signal1
    _filtered_signal_dyn = filtered_fft_dyn
    _filtered_signal_nondyn = out2

    clean_fft = np.fft.fft(_clean_signal)[:_clean_signal.size//2] / _clean_signal.size
    noisy_fft = np.fft.fft(_noisy_signal)[:_noisy_signal.size//2] / _noisy_signal.size
    filtered_fft_dyn = np.fft.fft(_filtered_signal_dyn)[:_filtered_signal_dyn.size//2] / _filtered_signal_dyn.size
    filtered_fft_nondyn = np.fft.fft(_filtered_signal_nondyn)[:_filtered_signal_nondyn.size//2] / _filtered_signal_nondyn.size

    freqs = np.fft.fftfreq(_clean_signal.size, t[1] - t[0])[:_clean_signal.size//2]

    plt.plot(freqs, np.abs(clean_fft), 'k--', alpha=.6, label='исходный сигнал')
    plt.plot(freqs, np.abs(noisy_fft), 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(freqs, np.abs(filtered_fft_dyn), 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(freqs, np.abs(filtered_fft_nondyn), 'b:', alpha=.4, label=r'$\left|W_1 (i F\omega) \mathcal{F}u(t)\right|$')

    plt.xlim(0, 50)
    plt.ylim(0, 1)

    plt.grid(which='major', linestyle=':', alpha=0.6)
    plt.legend()

    plt.savefig(f"../fig/1/1/a/conv/{i}.png")