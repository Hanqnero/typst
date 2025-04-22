%mkdir -p ../fig/1/1/T/func
%mkdir -p ../fig/1/1/T/fr

for i, N in enumerate((1e-3, 1e-2, 1e-1)):
    plt.figure()

    filtered_signal = apply_W_dynamic(t, signal, W1_tf(N))

    plt.plot(t, signal, 'r-', alpha=.5, linewidth=.9, label='зашумленный сигнал')
    plt.plot(t, filtered_signal, 'g-', alpha=.8, linewidth=.9, label='фильтрованный сигнал')
    plt.plot(t, clean_signal, 'k--', alpha=.6, linewidth=.9, label='исходный сигнал')
    plt.legend()

    plt.savefig(f"../fig/1/1/T/func/{i}.png")

    plt.figure()

    plot_freq_response(W1_tf(N), plt.gca(), t)

    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(100))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    plt.grid(which='minor', linestyle=':', alpha=0.4)
    plt.grid(which='major', linestyle='-', alpha=0.6)

    plt.legend([f'$T={N}$'])

    plt.savefig(f"../fig/1/1/T/fr/{i}.png")