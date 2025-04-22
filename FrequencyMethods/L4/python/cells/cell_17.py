fr = np.fft.fftfreq(t.size, d=t[1]-t[0])[:t.size//2]
_noisy_fft = np.abs(np.fft.fft(_noisy_signal)[:t.size//2])/t.size
_clean_fft = np.abs(np.fft.fft(g(t))[:t.size//2])/t.size
_filtered_fft = np.abs(np.fft.fft(apply_W_dynamic(t, _noisy_signal, _W))[:t.size//2])/t.size

plt.plot(fr, _noisy_fft, alpha=0.5, label='Зашумленный сигнал')
plt.plot(fr, _clean_fft, alpha=0.9, label='Исходный сигнал')
plt.plot(fr, _filtered_fft, alpha=0.7, linestyle=':', label='Фильтрованный сигнал')

plt.xlabel('$\\nu$')
plt.legend()

plt.xlim(left=0, right=50)


ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
plt.grid(which="major", linestyle="--", alpha=0.5)
plt.grid(which="minor", linestyle=":", alpha=0.3)

plt.savefig('../fig/1/2/comp/2.png')