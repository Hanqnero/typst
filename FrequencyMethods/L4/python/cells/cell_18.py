
fr = np.fft.fftfreq(t.size, d=t[1]-t[0])
_fr = fr[:t.size//2]
_filtered_fft = np.abs(np.fft.fft(apply_W_dynamic(t, _noisy_signal, _W))[:t.size//2]) / t.size
_product_fft = np.abs( W_poly(_W)(1j * np.pi*2 * fr) * np.fft.fft(_noisy_signal) )[:t.size//2] / t.size

plt.plot(_fr, _filtered_fft, alpha=0.5, linestyle='-', label='Фильтрованный сигнал')
plt.plot(_fr, _product_fft, alpha=0.7, linestyle='--', label='$W_2(i\\omega)\\mathcal{F}u(t)$')

plt.xlabel('$\\nu$')
plt.legend()
plt.xlim(left=0, right=50)

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
plt.grid(which="major", linestyle="--", alpha=0.5)
plt.grid(which="minor", linestyle=":", alpha=0.3)


plt.savefig('../fig/1/2/comp/3.png')
