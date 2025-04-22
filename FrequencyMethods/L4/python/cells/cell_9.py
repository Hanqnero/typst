%mkdir -p ../fig/1/1/comp

plt.figure()

y_out = apply_W_dynamic(t, signal, W1_tf(.01))
out2 = apply_W_nondynamic(t, signal, W1_tf(.01))


plt.plot(t, signal, 'r-', alpha=0.5, label='Зашумленный сигнал $u(t)$')
plt.plot(t, y_out, 'g-', alpha=.4, label='Фильрованный сигнал')
plt.plot(t, out2, 'b:', alpha=.4, label="$\\mathcal{F}^{-1}\\{W_{1}(i \\omega)\\mathcal{F}u(t)\\}$")

plt.xlabel('$t$')
plt.grid(which='major', linestyle=':', alpha=.3)
plt.legend()

plt.savefig("../fig/1/1/comp/1.png")
