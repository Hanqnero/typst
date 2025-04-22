fr = np.fft.fftfreq(t.size, t[1]-t[0])
fr = np.fft.fftshift(fr)

noisy_fft = np.abs(np.fft.fft(noisy_signal1))
noisy_fft = np.fft.fftshift(noisy_fft)

filtered_fft = np.abs(np.fft.fft(apply_W_dynamic(t, noisy_signal1, W1_tf(.01))))
filtered_fft = np.fft.fftshift(filtered_fft)

product_fft = W_poly(W1_tf(.01))(1j * 2*np.pi * fr) * noisy_fft
product_fft = np.abs(product_fft)

plt.figure()

plt.xlim(0, 100)
plt.xlabel("$t$")

plt.gca().get_xaxis().set_major_locator(plt.MultipleLocator(25))
plt.gca().get_xaxis().set_minor_locator(plt.MultipleLocator(5))
plt.gca().get_yaxis().set_major_locator(plt.MultipleLocator(.05))
plt.gca().get_yaxis().set_minor_locator(plt.MultipleLocator(.025))

plt.grid(which='major', linestyle='--', alpha=.5)
plt.grid(which='minor', linestyle=':', alpha=.3)

plt.plot(fr, filtered_fft/fr.size, alpha=.7, label='фильтрованный сигнал')
plt.plot(fr, product_fft/ fr.size, alpha=.99, linestyle=':', label='$W(i\\omega)\\mathcal{F}u(t)$')

plt.legend()
plt.savefig("../fig/1/1/comp/3.png")