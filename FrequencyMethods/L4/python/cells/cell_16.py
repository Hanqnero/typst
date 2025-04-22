omega0 = 2*np.pi * 20

a1 = 0
a2 = omega0**2
b1 = 10**3
b2 = omega0**2

_W = W2_tf(a1, a2, b1, b2)

_noisy_signal = noisy_signal1

filtered_signal_nonfair = apply_W_nondynamic(t, _noisy_signal, _W)
filtered_signal_fair = apply_W_dynamic(t, _noisy_signal, _W)

plt.plot(t, filtered_signal_fair, 'r-', alpha=.5, label='Динамическая фильтрация')
plt.plot(t, filtered_signal_nonfair, 'g--', alpha=.8, label='$\\mathcal{F}^{-1}(W(i\\omega)\\mathcal{F}u)$')

plt.xlabel("$t$")
plt.ylabel("Амплитуда сигнала")

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
plt.grid(which="major", linestyle="--", alpha=0.5)
plt.grid(which="minor", linestyle=":", alpha=0.3)
plt.legend()

%mkdir -p ../fig/1/2/comp

plt.savefig('../fig/1/2/comp/1.png')