import os
import functools
import time

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from numpy.fft import fft, ifft, fftshift, ifftshift, fftfreq


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {(end_time - start_time)*1000:.4f} ms")
        return result

    return wrapper


plt.rcParams["figure.figsize"] = FIGSIZE = (
    200 / 25.4,
    200 / (16 / 9) / 25.4,
)  # 16 by 9 aspect & 200mm width

FIGSIZE_WIDE = (
    300 / 25.4,
    300 / 2.5 / 25.4,
)  # 5 by 2 aspect & 200mm width


plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams["font.family"] = "serif"
plt.rcParams["figure.dpi"] = 100

PI = np.pi
TAU = 2 * np.pi


def add_grid(ax: Axes):
    ax.grid(which="major", linestyle="-", alpha=0.6)
    ax.grid(which="minor", linestyle=":", alpha=0.4)


# === Task 1 ===

t = np.linspace(-2, 2, 1000)

rect = lambda t: np.where(np.abs(t) < 0.5, 1, 0)
Pi = rect(t)

Pi_hat_true = np.sinc(t * PI)

os.makedirs("../fig/task1/", exist_ok=True)

plt.figure()
plt.plot(t, Pi)
plt.xlabel("t")
plt.ylabel(r"$\Pi(t)$")
plt.savefig(r"../fig/task1/Pi.png")
plt.close()

plt.figure()
plt.plot(t, Pi_hat_true)
plt.savefig(r"../fig/task1/Pi_hat_true.png")
plt.close()


# === Task 1.1
def trapz_ft(signal, t, v):
    dt = t[1] - t[0]
    y = signal * np.exp(-1j * TAU * v[..., np.newaxis] * t)
    integral = np.trapezoid(y, dx=dt, axis=1)

    assert integral.shape == v.shape
    return integral


def trapz_ift(ft, t, v):
    dv = v[1] - v[0]
    y = ft * np.exp(1j * TAU * t[..., np.newaxis] * v)
    integral = np.trapezoid(y, dx=dv, axis=1)

    assert integral.shape == t.shape
    return np.real(integral)


def task11(T, dt, V, dv):
    t = np.arange(-T / 2, T / 2, dt)
    v = np.arange(-V / 2, V / 2, dv)

    t_fine = np.arange(-T / 2, T / 2, dt / 10)
    v_fine = np.arange(-V / 2, V / 2, dv / 10)

    signal = rect(t)

    global i
    os.makedirs(f"../fig/task1/1.1/{i}", exist_ok=True)

    @timeit
    def perform_ft():
        ft = trapz_ft(signal, t, v)
        recon = trapz_ift(ft, t, v)
        return ft, recon

    ft_, recon_ = perform_ft()

    true_ft = np.sinc(v_fine)
    true_rect = rect(t_fine)

    # Ft
    plt.figure()
    plt.margins(0.05, tight=True)
    plt.xlabel(r"$\nu$")

    plt.plot(v, np.real(ft_), "--", label=r"$Re F(\nu)$")
    plt.plot(v, np.imag(ft_), label=r"$Im F(\nu)$")
    plt.plot(v_fine, true_ft, "-", color="grey", alpha=0.4, label=r"$\hat{\Pi}(\nu)$")
    plt.legend()
    add_grid(plt.gca())
    plt.savefig(f"../fig/task1/1.1/{i}/F.png")
    plt.close()

    # Recon
    plt.figure()
    plt.xlim(t[0], t[-1])
    # plt.margins(0.05, tight=True)
    plt.xlabel(r"$t$")

    plt.plot(t, np.real(recon_), "r-", label=r"восстановленный")
    plt.plot(t_fine, true_rect, "g--", label=r"$\Pi(t)$")
    plt.legend()
    add_grid(plt.gca())

    plt.savefig(f"../fig/task1/1.1/{i}/f_recon.png")
    plt.close()


# === Task 1.2 ===
def task12(T, dt):
    global i
    os.makedirs(f"../fig/task1/1.2/{i}", exist_ok=True)

    t = np.arange(-T / 2, T / 2, dt)
    v = fftshift(fftfreq(t.size, dt))
    V = v[-1] - v[0]

    v_min = -20 if v[0] < -20 else v[0]
    v_max = 20 if v[-1] > 20 else v[-1]

    t_fine = np.arange(-T / 2, T / 2, dt / 10)
    signal = rect(t)
    signal_fine = rect(t_fine)

    v_fine = np.arange(-V / 2, V / 2, 1 / T / 10)
    sinc_fine = np.sinc(v_fine)

    @timeit
    def perform_fft():
        ft = fftshift(fft(signal, norm="ortho"))
        recon = ifft(ifftshift(ft), norm="ortho")
        return ft, recon

    ft_, recon_ = perform_fft()

    # FT
    plt.figure()
    plt.xlim(-V / 2, V / 2)
    plt.xlabel(r"$\nu$")

    plt.plot(v, np.real(ft_), label=r"$F(\nu)$")
    plt.plot(v_fine, sinc_fine, label=r"$\text{sinc}(\nu)$")
    plt.legend()
    add_grid(plt.gca())
    plt.savefig(f"../fig/task1/1.2/{i}/F.png")
    plt.close()

    # Recon
    plt.figure()
    plt.xlim((-T / 2, T / 2))
    plt.margins(0.05, tight=True)
    plt.xlabel(r"$t$")

    plt.plot(t_fine, signal_fine, label=r"$\Pi(t)$")
    plt.plot(t, np.real(recon_), "--", label="Восстановленный")
    add_grid(plt.gca())
    plt.legend()
    plt.savefig(f"../fig/task1/1.2/{i}/f_recon.png")
    plt.close()


# === Task 1.4 ===


def ft_fft_normalized(signal, t, v, c=None, return_c=False):
    T = t[-1] - t[0]
    dt = t[1] - t[0]

    c = c if c is not None else dt * np.exp(-1j * TAU * v * -T / 2)
    # c = c or dt * np.pow(-1, np.arange(0, v.size))

    ft = c * fftshift(fft(signal))

    if return_c:
        return ft, c
    return ft


def ift_fft_normalized(ft, t, v, c=None):
    T = t[-1] - t[0]
    dt = t[1] - t[0]

    c = c if c is not None else dt * np.exp(-1j * TAU * v * -T / 2)

    recon = ifft(ifftshift(ft / c))
    return np.real(recon)


def task141(T, dt):
    """Графики умного fft"""

    t = np.arange(-T / 2, T / 2, dt)
    t_fine = np.arange(-T / 2, T / 2, dt / 10)
    v = fftshift(fftfreq(t.size, dt))
    v_fine = np.arange(-1 / dt / 2, 1 / dt / 2, 1 / T / 10)
    sinc_fine = np.sinc(v_fine)

    signal = rect(t)
    signal_fine = rect(t_fine)

    ft_fft, c = ft_fft_normalized(signal, t, v, return_c=True)
    recon_fft = ift_fft_normalized(ft_fft, t, v, c)

    ft_raw = fftshift(fft(signal, norm="ortho"))
    recon_raw = ifft(ifftshift(ft_raw), norm="ortho")
    recon_raw = np.real(recon_raw)

    ft_trapz = trapz_ft(signal, t, v)
    recon_trapz = trapz_ift(ft_trapz, t, v)

    global i
    os.makedirs(f"../fig/task1/1.4/new_method/{i}", exist_ok=True)

    params_text = """\
$T = {T:.3f}\\:с$
$dt = {dt:.3f}\\:С$
$V = {V:.3f}\\:Гц$
$\\mathrm{{d}} v = {dv:.3f}\\:Гц$"""
    params_text = params_text.format(T=T, dt=dt, V=1 / (dt), dv=1 / T)

    v_min = -20 if v.min() < -20 else v.min()
    v_max = 20 if v.max() > 20 else v.max()

    # F
    plt.figure()
    plt.xlim(v_min, v_max)
    plt.plot(v, np.real(ft_fft), "r--", alpha=0.6, label=r"$Re \overline{F}$")
    plt.plot(v, np.imag(ft_fft), "b--", alpha=0.6, label=r"$Im \overline{F}$")
    plt.plot(v_fine, sinc_fine, "g-", alpha=0.6, label=r"$\hat{\Pi}(t)$")
    plt.text(
        0.80,
        0.50,
        params_text,
        transform=plt.gca().transAxes,
        bbox=dict(
            boxstyle="round,pad=.3", edgecolor="grey", facecolor="white", alpha=0.6
        ),
    )
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"../fig/task1/1.4/new_method/{i}/F.png")
    plt.close()

    # Recon
    plt.figure()
    plt.xlim((-2, 2))
    plt.plot(t_fine, signal_fine, "g-", alpha=0.6, label=r"Исходный сигнал")
    plt.plot(
        t, np.real(recon_fft), "r--", alpha=0.6, label=r"$\mathcal{F}^{-1}\overline{F}$"
    )
    plt.text(
        0.80,
        0.50,
        params_text,
        transform=plt.gca().transAxes,
        bbox=dict(
            boxstyle="round,pad=.3", edgecolor="grey", facecolor="white", alpha=0.6
        ),
    )
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"../fig/task1/1.4/new_method/{i}/recon.png")
    plt.close()

    os.makedirs("../fig/task1/1.4/F_comp/", exist_ok=True)

    v_min = -20 if v.min() < -20 else v.min()
    v_max = 20 if v.max() > 20 else v.max()

    # Compare new FFT, raw FFT, trapz
    plt.figure()
    plt.xlim(v_min, v_max)
    plt.plot(v, np.real(ft_raw), "g-", alpha=0.3, label="FFT")
    plt.plot(v, np.real(ft_fft), "r--", alpha=0.4, label="Умный FFT")
    plt.plot(v, np.real(ft_trapz), "b:", alpha=0.6, label="Числ. интегр.")
    plt.text(
        0.79,
        0.10,
        params_text,
        transform=plt.gca().transAxes,
        bbox=dict(
            boxstyle="round,pad=.3", edgecolor="grey", facecolor="white", alpha=0.6
        ),
    )
    plt.legend()
    plt.savefig(f"../fig/task1/1.4/F_comp/{i}.png")
    plt.close()

    os.makedirs(f"../fig/task1/1.4/recon_comp/", exist_ok=True)

    # Compare Recons
    plt.figure()
    plt.xlim(-2, 2)
    plt.plot(t, recon_raw, "g-", alpha=0.6, label="FFT")
    plt.plot(t, recon_fft, "r--", alpha=0.6, label="Умный FFT")
    plt.plot(t, recon_trapz, ":", color="purple", alpha=0.5, label="Числ. интегр.")
    plt.text(
        0.79,
        0.10,
        params_text,
        transform=plt.gca().transAxes,
        bbox=dict(
            boxstyle="round,pad=.3", edgecolor="grey", facecolor="white", alpha=0.6
        ),
    )
    plt.legend()
    plt.savefig(f"../fig/task1/1.4/recon_comp/{i}.png")
    plt.close()


# === Task 2 ===


def y1_func(t, a1, a2, phi1, phi2, w1, w2):
    return a1 * np.sin(w1 * t + phi1) + a2 * np.sin(w2 * t + phi2)


def y2_func(t, b):
    return np.sinc(b * t)


def task21(T=5, dt=1e-4):
    """Построить графики непрерывных функций"""

    os.makedirs("../fig/task2", exist_ok=True)

    global a1, a2, phi1, phi2, w1, w2
    global b
    params = [a1, a2, phi1, phi2, w1, w2]

    t = np.arange(-T / 2, T / 2, dt)
    y1_cont = y1_func(t, *params)
    y2_cont = y2_func(t, b)

    v = fftshift(fftfreq(t.size, dt))

    y1_ft = ft_fft_normalized(y1_cont, t, v)
    y2_ft = ft_fft_normalized(y2_cont, t, v)

    # y1
    plt.figure(figsize=FIGSIZE_WIDE)
    plt.subplot(1, 2, 1)
    plt.plot(t, y1_cont, label=r"$y_1(t)$ (непрерывная)")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y_1(t)$")
    plt.xlim([-0.3, 0.3])
    plt.legend()
    add_grid(plt.gca())

    plt.subplot(1, 2, 2)
    plt.plot(v, np.abs(y1_ft), label=r"$\hat{y}_1(\nu)$ (непрерывная)")
    plt.xlabel(r"$\nu$")
    plt.ylabel(r"$\hat{y}_1(\nu)$")
    plt.xlim([-20, 20])
    plt.legend()
    add_grid(plt.gca())

    plt.tight_layout()
    plt.savefig("../fig/task2/y1_cont.png")
    plt.close()

    # y2
    plt.figure(figsize=FIGSIZE_WIDE)
    plt.subplot(1, 2, 1)
    plt.plot(t, y2_cont, label=r"$y_2(t)$ (непрерывная)")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y_2(t)$")
    plt.xlim([-0.5, 0.5])
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(v, np.abs(y2_ft), label=r"$\hat{y}_2(\nu)$ (непрерывная)")
    plt.xlabel(r"$\nu$")
    plt.ylabel(r"$\hat{y}_2(\nu)$")
    plt.xlim([-10, 10])
    plt.legend()

    plt.tight_layout()
    plt.savefig("../fig/task2/y2_cont.png")
    plt.close()


def interp(ts, ys, t, dt):
    """Интерполировать семплированный сигнал `y`
    в моментах `ts` до времени `t`"""
    assert ts.size == ys.size
    x = (t[None, :] - ts[:, None]) / dt  # (N, M)
    return ys @ np.sinc(x)  # N @ (N, M) -> M


def test_inter():
    dt = 0.05
    t = np.arange(-1, 1, 0.001)
    ts = np.arange(-1, 1, dt)

    y = np.sin(TAU * 5 * t)
    ys = np.sin(TAU * 5 * ts)

    plt.figure()
    plt.plot(t, y, alpha=0.3, color="black")
    plt.stem(ts, ys)
    y_rec = interp(ts, ys, t, dt)

    assert t.size == y_rec.size
    plt.plot(t, y_rec, color="red", linestyle="--")

    plt.show()
    plt.close()


def task22(T=5, dt=1e-4):
    """Построить графики сеплированных функций"""
    global i

    global a1, a2, phi1, phi2, w1, w2
    global b
    params = [a1, a2, phi1, phi2, w1, w2]

    fig_root = f"../fig/task2/{i}"
    print(fig_root)
    os.makedirs(fig_root, exist_ok=True)

    t_cont = np.arange(-T / 2, T / 2, 1e-4)
    y1_cont = y1_func(t_cont, *params)
    y2_cont = y2_func(t_cont, b)
    v_cont = fftshift(fftfreq(t_cont.size, 1e-4))
    y1_cont_ft = ft_fft_normalized(y1_cont, t_cont, v_cont)
    y2_cont_ft = ft_fft_normalized(y2_cont, t_cont, v_cont)

    t_samp = np.arange(-T / 2, T / 2, dt)
    y1_samp = y1_func(t_samp, *params)
    y2_samp = y2_func(t_samp, b)
    v_samp = fftshift(fftfreq(t_samp.size, dt))
    y1_samp_ft = ft_fft_normalized(y1_samp, t_samp, v_samp)
    y2_samp_ft = ft_fft_normalized(y2_samp, t_samp, v_samp)

    y1_int = interp(t_samp, y1_samp, t_cont, dt)
    y2_int = interp(t_samp, y2_samp, t_cont, dt)
    y1_int_ft = ft_fft_normalized(y1_int, t_cont, v_cont)
    y2_int_ft = ft_fft_normalized(y2_int, t_cont, v_cont)

    y1_labels = ["исходная", "семплированная", "интерполяция"]
    y2_labels = y1_labels

    for j, (
        y_samp,
        y_cont,
        y_int,
        labels,
        limits,
        y_ft_cont,
        y_ft_samp,
        y_ft_int,
        limits2,
    ) in enumerate(
        [
            (
                y1_samp,
                y1_cont,
                y1_int,
                y1_labels,
                [-0.3, 0.3],
                y1_cont_ft,
                y1_samp_ft,
                y1_int_ft,
                [-20, 20],
            ),
            (
                y2_samp,
                y2_cont,
                y2_int,
                y2_labels,
                [-0.5, 0.5],
                y2_cont_ft,
                y2_samp_ft,
                y2_int_ft,
                [-10, 10],
            ),
        ],
        start=1,
    ):

        title_text1 = f"$y_{{{j}}}(t)$: $T={T}$ $dt={dt}$ $f_s={1/dt:.1f}$"
        title_text2 = f"$\\hat{{y}}_{{{j}}}(t)$: $T={T}$ $dt={dt}$ $f_s={1/dt:.1f}$"

        plt.figure(figsize=FIGSIZE_WIDE)
        plt.subplot(1, 2, 1)
        plt.plot(
            t_cont,
            y_cont,
            label=labels[0],
            linestyle="--",
            color="black",
            alpha=0.6,
        )
        ml, sl, bl = plt.stem(
            t_samp,
            y_samp,
            "b-",
            markerfmt="bo",
            basefmt=" ",
            label=labels[1],
        )
        plt.setp(ml, markersize=3, alpha=0.6)
        plt.setp(bl, alpha=0)
        plt.setp(sl, linewidth=1)

        plt.plot(t_cont, y_int, "r:", label=labels[2], alpha=0.6)

        add_grid(plt.gca())
        plt.xlim(limits)
        plt.title(title_text1)
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(
            v_cont,
            np.abs(y_ft_cont),
            label=labels[0],
            color="black",
            linestyle="--",
            alpha=0.6,
        )
        plt.plot(
            v_samp,
            np.abs(y_ft_samp),
            label=labels[1],
            color="blue",
            linestyle="--",
            alpha=0.6,
        )
        plt.plot(
            v_cont,
            np.abs(y_ft_int),
            label=labels[2],
            color="red",
            linestyle=":",
            alpha=0.6,
        )

        add_grid(plt.gca())
        plt.xlim(limits2)
        plt.legend()

        plt.title(title_text2)
        plt.tight_layout()
        plt.savefig(f"../fig/task2/{i}/y{j}_comp.png")
        plt.close()


if __name__ == "__main__":
    # === Task 1.1 ===
    for i, (T, dt, V, dv) in enumerate(
        (
            (2, 0.005, 10, 0.05),
            (5, 0.005, 60, 0.05),  # small T
            (2, 0.05, 10, 0.5),  # small V  -> recon smoother
            (5, 0.05, 60, 0.5),  # large dt -> ft repeants & recon wrong
        )
    ):
        print(f"task 1.1 iteration {i}")
        task11(T, dt, V, dv)

    # === Task 1.2 ===
    for i, (T, dt) in enumerate(
        (
            (4, 0.005),
            (4, 0.05),  # big dt -> small V
            (8, 0.005),  # big T -> small dv
        )
    ):
        print(f"task 1.2 iteration {i}")
        task12(T, dt)

    # === Task 1.4.1 ===
    for i, (T, dt) in enumerate(
        (
            (4, 0.004),
            (4, 0.080),  # small dt -> small V   NOTE: V = 1/(dt)
            (8, 0.004),  # big T -> small dv     NOTE: dv = 1/T
        )
    ):
        task141(T, dt)

    # === Task 2 ===
    a1, a2, phi1, phi2, w1, w2 = params = 1, 3, 2, 5, TAU * 10, TAU * 15
    b = 10

    # == original functions
    task21()

    # comparison
    for i, (T, dt) in enumerate(
        (
            (2, 0.02),
            (5, 0.01),
            (10, 0.005),
            (5, 0.15),
        )
    ):
        task22(T, dt)
