%mkdir -p ../fig/1/1/T/func
%mkdir -p ../fig/1/1/T/fr
%mkdir -p ../fig/1/1/T/conv

for i, N in enumerate((1e-3, 1e-2, 1e-1)):
    # =======================
    # Сравненение результатов
    # =======================
    plt.figure()

    filtered_fft_dyn = apply_W_dynamic(t, signal, W1_tf(N))
    out2 = apply_W_nondynamic(t, signal, W1_tf(N))

    plt.plot(t, signal, 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(t, filtered_fft_dyn, 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(t, out2, 'b:', alpha=.4, label="$\\mathcal{F}^{-1}\\{W_{1}(i \\omega)\\mathcal{F}u(t)\\}$")
    plt.plot(t, clean_signal, 'k--', alpha=.6, label='исходный сигнал')
    plt.legend()

    plt.xlabel('$t$')
    plt.grid(which='major', linestyle=':', alpha=0.6)

    plt.savefig(f"../fig/1/1/T/func/{i}.png")

    # ===========
    # АЧХ Фильтра 
    # ===========
    plt.figure()

    plot_freq_response(W1_tf(N), plt.gca(), t)

    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(100))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    plt.grid(which='minor', linestyle=':', alpha=0.4)
    plt.grid(which='major', linestyle='-', alpha=0.6)

    plt.legend([f'$T={N}$'])

    plt.savefig(f"../fig/1/1/T/fr/{i}.png")


    # ======
    # Образы
    # ======

    plt.figure()
    
    _clean_singal = clean_signal
    clean_fft = np.fft.fft(_clean_singal)[:_clean_singal.size//2] / _clean_singal.size

    _noisy_signal = signal
    noisy_fft = np.fft.fft(_noisy_signal)[:_noisy_signal.size//2] / _noisy_signal.size

    _filtered_signal_dyn = filtered_fft_dyn
    filtered_fft_dyn = np.fft.fft(_filtered_signal_dyn)[:_filtered_signal_dyn.size//2] / _filtered_signal_dyn.size

    _filtered_signal_nondyn = out2
    filtered_fft_nondyn = np.fft.fft(_filtered_signal_nondyn)[:_filtered_signal_nondyn.size//2] / _filtered_signal_nondyn.size

    freqs = np.fft.fftfreq(_clean_singal.size, t[1] - t[0])[:_clean_singal.size//2]

    plt.plot(freqs, np.abs(clean_fft), 'k--', alpha=.6, label='исходный сигнал')
    plt.plot(freqs, np.abs(noisy_fft), 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(freqs, np.abs(filtered_fft_dyn), 'g-', alpha=.5, label='фильтрованный сигнал')
    plt.plot(freqs, np.abs(filtered_fft_nondyn), 'b:', alpha=.4, label=r'$\left|W_1 (i F\omega) \mathcal{F}u(t)\right|$')

    plt.xlim(0, 50)
    plt.ylim(0, 0.1)

    plt.grid(True, which='major', linestyle=':', alpha=0.6)
    plt.legend()

    plt.savefig(f"../fig/1/1/T/conv/{i}.png")
