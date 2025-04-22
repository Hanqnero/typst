%mkdir -p ../fig/1/1/a

noise = xi(t)
w = W1_tf(.01)

for i, a in enumerate((1,2,3), start=3):

    clean_signal1 = g_(a, 2, 3)(t)
    noisy_signal1 = clean_signal1 + noise

    filtered_signal = apply_W_dynamic(t, noisy_signal1, w)

    plt.figure(num=i)
    plt.plot(t, noisy_signal1, 'r-', alpha=.5, label='зашумленный сигнал')
    plt.plot(t, filtered_signal, 'g-', label='фильтрованный сигнал')
    plt.plot(t, clean_signal1, 'k--', linewidth=1.5, alpha=.6, label='исходный сигнал')
    plt.legend()

    plt.savefig(f"../fig/1/1/a/{i}.png")