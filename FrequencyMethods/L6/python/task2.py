#!/usr/bin/env ~/.pyenv/jupyter3.13/bin/python

# Константы
from numpy.fft import fft2, ifft2, fftshift
from scipy.signal import convolve2d
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# Определяем директорию скрипта и пути
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Путь к файлу RGB-изображения
IMAGE_PATH = os.path.join(SCRIPT_DIR, '../sup/15.png')
# Директория для сохранения результатов
FIG_DIR = os.path.join(SCRIPT_DIR, '../fig/task2')


# Создаём директорию для сохранения, если её нет
os.makedirs(FIG_DIR, exist_ok=True)

# 1. Загрузка и подготовка изображения (RGB)
img_color = Image.open(IMAGE_PATH).convert('RGB')
image = np.array(img_color, dtype=np.float64) / 255.0  # форма (H, W, 3)
H, W, C = image.shape  # C == 3

# 2. Определение ядер свёртки


def gaussian_kernel(N):
    sigma = (N - 1) / 6.0
    ax = np.arange(N) - (N - 1) / 2.0
    xx, yy = np.meshgrid(ax, ax)
    A = np.exp(- (xx**2 + yy**2) / (2 * sigma**2))
    return A / np.sum(A)


def box_kernel(N):
    A = np.ones((N, N), dtype=np.float64)
    return A / np.sum(A)


SHARPEN_KERNEL = np.array([[0, -1,  0],
                           [-1,  5, -1],
                           [0, -1,  0]], dtype=np.float64)
EDGE_KERNEL = np.array([[-1, -1, -1],
                        [-1,  8, -1],
                        [-1, -1, -1]], dtype=np.float64)
# EMBOSS_KERNEL = np.array([[-2, -1,  0],
#                           [-1,  1,  1],
#                           [0,  1,  2]], dtype=np.float64)

EMBOSS_KERNEL = np.array([[1, 0, 0,  0, 0],
                          [0, 1, 0,  0, 0],
                          [0, 0, 0,  0, 0],
                          [0, 0, 0, -1, 0],
                          [0, 0, 0, 0, -1]], dtype=np.float64)

kernels = {}
for N in [7, 11, 17]:
    kernels[f'gaussian_{N}'] = gaussian_kernel(N)
    kernels[f'box_{N}'] = box_kernel(N)
kernels['sharpen_3'] = SHARPEN_KERNEL
kernels['edge_3'] = EDGE_KERNEL
kernels['emboss_3'] = EMBOSS_KERNEL

# 3. Пространственная свёртка изображения (RGB -> RGB)
conv_spatial = {}
for name, K in kernels.items():
    kH, kW = K.shape
    out_H, out_W = H + kH - 1, W + kW - 1
    conv_full_rgb = np.zeros((out_H, out_W, C), dtype=np.float64)
    for c in range(C):
        conv_full_rgb[..., c] = convolve2d(
            image[..., c], K, mode='full', boundary='fill', fillvalue=0
        )
    conv_spatial[name] = conv_full_rgb

# 4. Фурье-образы изображения и ядер (RGB)


def log_magnitude_spectrum_2d(F2d):
    mag = np.abs(F2d)
    log_mag = np.log1p(mag)
    return (log_mag - log_mag.min()) / (log_mag.max() - log_mag.min())


F_kernels = {}
F_kernels_raw = {}
for name, K in kernels.items():
    kH, kW = K.shape
    out_shape = (H + kH - 1, W + kW - 1)
    F_K = fft2(K, s=out_shape)
    F_K_shifted = fftshift(F_K)
    F_kernels[name] = log_magnitude_spectrum_2d(F_K_shifted)
    F_kernels_raw[name] = F_K

# 5. Фильтрация путем умножения спектров
conv_freq = {}
for name, K in kernels.items():
    kH, kW = K.shape
    out_shape = (H + kH - 1, W + kW - 1)
    out_H, out_W = out_shape
    image_padded = np.zeros((C, out_H, out_W), dtype=np.float64)
    for c in range(C):
        image_padded[c, :H, :W] = image[..., c]
    F_I_padded = fft2(image_padded)
    F_K = F_kernels_raw[name][None, ...]
    F_prod = F_I_padded * F_K
    result_ifft = ifft2(F_prod)
    conv_freq[name] = np.real(result_ifft).transpose(1, 2, 0)

# 6. Визуализация и сохранение результатов
# сохраняем исходное изображение
plt.imsave(os.path.join(FIG_DIR, 'original_RGB.png'), image)

# вычисляем и сохраняем модуль спектра исходного
# изображения по каждому каналу
log_F_image = np.zeros((H, W, C), dtype=np.float64)
for c in range(C):
    F_c = fftshift(fft2(image[..., c]))
    log_F_image[..., c] = log_magnitude_spectrum_2d(F_c)
plt.imsave(os.path.join(FIG_DIR, 'original_spectrum_RGB.png'),
           np.clip(log_F_image, 0, 1))

for name, K in kernels.items():
    kernel_dir = os.path.join(FIG_DIR, name)
    os.makedirs(kernel_dir, exist_ok=True)
    kH, kW = K.shape
    out_H, out_W = H + kH - 1, W + kW - 1

    # сохраняем лог-модуль спектра ядра
    plt.imsave(
        os.path.join(kernel_dir, f'{name}_kernel_spectrum.png'),
        F_kernels[name], cmap='gray'
    )
    # сохраняем результат пространственной свёртки (центр)
    conv_sp = conv_spatial[name]
    start_i = (conv_sp.shape[0] - H) // 2
    start_j = (conv_sp.shape[1] - W) // 2
    conv_sp_center = conv_sp[start_i:start_i + H, start_j:start_j + W, :]
    plt.imsave(
        os.path.join(kernel_dir, f'{name}_spatial_conv.png'),
        np.clip(conv_sp_center, 0, 1)
    )
    # сохраняем лог-модуль спектра после пространственной свёртки
    log_F_conv_sp_rgb = np.zeros((out_H, out_W, C), dtype=np.float64)
    for c in range(C):
        Fc = fftshift(fft2(conv_sp[..., c], s=(out_H, out_W)))
        log_F_conv_sp_rgb[..., c] = log_magnitude_spectrum_2d(Fc)
    plt.imsave(
        os.path.join(kernel_dir, f'{name}_spectrum_after_spatial.png'),
        np.clip(log_F_conv_sp_rgb, 0, 1)
    )
    # сохраняем результат фильтрации через Фурье (центр)
    conv_fr = conv_freq[name]
    start_i2 = (conv_fr.shape[0] - H) // 2
    start_j2 = (conv_fr.shape[1] - W) // 2
    conv_fr_center = conv_fr[start_i2:start_i2 + H, start_j2:start_j2 + W, :]
    plt.imsave(
        os.path.join(kernel_dir, f'{name}_freq_filter.png'),
        np.clip(conv_fr_center, 0, 1)
    )

# 7. Сравнение качества блочного и гауссовского размытия для N = 13 (RGB)
name_gauss = 'gaussian_17'
name_box = 'box_17'
compare_dir = os.path.join(FIG_DIR, 'compare_gauss17_box17')
os.makedirs(compare_dir, exist_ok=True)
conv_gauss_full = conv_spatial[name_gauss]
start_i = (conv_gauss_full.shape[0] - H) // 2
start_j = (conv_gauss_full.shape[1] - W) // 2
conv_gauss_center = conv_gauss_full[start_i:start_i +
                                    H, start_j:start_j + W, :]
plt.imsave(
    os.path.join(compare_dir, 'gaussian_17_spatial.png'),
    np.clip(conv_gauss_center, 0, 1)
)
conv_box_full = conv_spatial[name_box]
start_i = (conv_box_full.shape[0] - H) // 2
start_j = (conv_box_full.shape[1] - W) // 2
conv_box_center = conv_box_full[start_i:start_i + H, start_j:start_j + W, :]
plt.imsave(
    os.path.join(compare_dir, 'box_17_spatial.png'),
    np.clip(conv_box_center, 0, 1)

)

# vim:set ai tw=70 sw=4 ts=4 :
