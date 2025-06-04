import os
import numpy as np
import numpy.fft as fft
from PIL import Image
import matplotlib.pyplot as plt

# --- Настройки: пути и создание папки для результатов ---
os.makedirs("../fig/task1", exist_ok=True)
os.chdir(os.path.dirname(__file__))
img_path            = "../sup/15.png"
out_mag_path        = "../fig/task1/out.abs.png"        # оригинальный лог-модуль
edited_spec_path    = "../sup/in.abs.png"         # отредактированный спектр (визуализация)
orig_path           = "../fig/task1/orig.png"           # оригинал
recon_path          = "../fig/task1/recon_color.png"    # восстановленное

# === БЛОК 1: Загрузка и сохранение оригинала ===
img0 = Image.open(img_path).convert("RGB")
orig = np.asarray(img0, dtype=np.float64) / 255.0   # shape (H, W, 3)
# сохраняем оригинал
Image.fromarray((orig * 255).astype(np.uint8), mode="RGB").save(orig_path)
print(f"Сохранён оригинал: {orig_path}")

# === БЛОК 2: Прямое БПФ и центрирование ===
F = fft.fftshift(fft.fft2(orig, axes=(0,1)), axes=(0,1))

# === БЛОК 3: Модуль и фаза ===
mag   = np.abs(F)
phase = np.angle(F)

# === БЛОК 4: Визуализация оригинального спектра ===
log_mag   = np.log(mag + 1.0)
log_min   = log_mag.min(axis=(0,1), keepdims=True)
log_max   = log_mag.max(axis=(0,1), keepdims=True)
log_range = log_max - log_min
log_norm  = (log_mag - log_min) / log_range

# сохраняем визуализацию лог-модуля спектра
out_img = (log_norm * 255).astype(np.uint8)
Image.fromarray(out_img, mode="RGB").save(out_mag_path)
print(f"Сохранён лог-модуль спектра: {out_mag_path}")

# --- Редактирование верхних гармоник вручную:
#      отредактируйте ../fig/out.abs.png и сохраните как ../fig/in.abs.png ---

# === БЛОК 5: Загрузка отредактированного спектра и сохранение ===
in_img  = Image.open(edited_spec_path).convert("RGB")
in_norm = np.asarray(in_img, dtype=np.float64) / 255.0
# сохраняем визуализацию отредактированного спектра
Image.fromarray((in_norm * 255).astype(np.uint8), mode="RGB").save(edited_spec_path)
print(f"Сохранён отредактированный спектр: {edited_spec_path}")

# === БЛОК 6: Обратное преобразование визуализации → «сырые» mag ===
log_mag_edit = in_norm * log_range + log_min
mag_edit     = np.exp(log_mag_edit) - 1.0

# === БЛОК 7: Сборка спектра и обратное БПФ ===
F_edit  = mag_edit * np.exp(1j * phase)
img_edit = fft.ifft2(fft.ifftshift(F_edit, axes=(0,1)), axes=(0,1)).real
img_edit = np.clip(img_edit, 0.0, 1.0)
# сохраняем восстановленное цветное изображение
Image.fromarray((img_edit * 255).astype(np.uint8), mode="RGB").save(recon_path)
print(f"Сохранено восстановленное изображение: {recon_path}")

# === БЛОК 8: Визуализация в сетке 2×2 ===
fig, axes = plt.subplots(2, 2, figsize=(10,10))

axes[0,0].imshow(orig);       axes[0,0].set_title("Оригинал");             axes[0,0].axis("off")
axes[0,1].imshow(log_norm);   axes[0,1].set_title("Лог-модуль (оригинал)"); axes[0,1].axis("off")
axes[1,0].imshow(in_norm);    axes[1,0].set_title("Лог-модуль (edited)");  axes[1,0].axis("off")
axes[1,1].imshow(img_edit);   axes[1,1].set_title("Восстановлено");        axes[1,1].axis("off")

plt.tight_layout()
plt.show()
