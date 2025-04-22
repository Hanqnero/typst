plt.figure()

clean_signal = g(t)
noisy_signal1 = g(t) + xi(t)
filtered_signal = apply_W_dynamic(t, noisy_signal1, W1_tf(0.01))

fr = np.fft.fftfreq(t.size, d=t[1]-t[0])
fr = np.fft.fftshift(fr)

clean_fft = np.abs(np.fft.fft(clean_signal))/t.size
clean_fft = np.fft.fftshift(clean_fft)

noisy_fft = np.abs(np.fft.fft(noisy_signal1))/t.size
noisy_fft = np.fft.fftshift(noisy_fft)

filtered_fft = np.abs(np.fft.fft(filtered_signal))/t.size
filtered_fft = np.fft.fftshift(filtered_fft)

plt.xlim(0, 100)

plt.plot(fr, clean_fft, alpha=.9)
plt.plot(fr, noisy_fft, alpha=.5)
plt.plot(fr, filtered_fft, alpha=.7, linestyle=':')

plt.xlabel('$\\nu$')
plt.legend(['Исходный сигнал', 'Зашумленный сигнал', 'Фильтрованный сигнал'])


plt.gca().get_xaxis().set_major_locator(plt.MultipleLocator(20))
plt.gca().get_xaxis().set_minor_locator(plt.MultipleLocator(10))
plt.gca().get_yaxis().set_major_locator(plt.MultipleLocator(.05))
plt.gca().get_yaxis().set_minor_locator(plt.MultipleLocator(.025))

plt.grid(which='major', linestyle='--', alpha=.5)
plt.grid(which='minor', linestyle=':', alpha=.3)

plt.savefig("../fig/1/1/comp/2.png")
