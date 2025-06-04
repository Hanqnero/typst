# АЧХ
def freq_response(W, t):
    poly = W_poly(W)

    sr = t[1] - t[0]
    N = t.size

    fr = np.fft.fftfreq(N, sr)
    fr = np.fft.fftshift(fr)

    return fr, np.abs(poly(1j*np.pi*2*fr))


#график АЧХ
def plot_freq_response(W, ax, t):  
    fr, response = freq_response(W, t)

    ax.set_xlabel('$\\nu$')
    ax.set_ylabel('$|W(i\\omega)|$')
    ax.plot(fr, response)

    plt.grid(which='major', linestyle='-', alpha=0.6)
    ax.set_xlim(left=0, right=fr[-1])

plot_freq_response(W1_tf(.01), plt.axes(), t)