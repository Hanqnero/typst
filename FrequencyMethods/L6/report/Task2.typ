Для этого задания выбрали то же изображение, что и в первом задании.

#figure(
  image("../sup/15.png", height: 10cm),
  caption: [Исходное изображение]
)

Рассмотрим, как повлияют различные ядра для свертки на взятое изображение.
Рассмотрим ядра:

#let _rect = box(stroke: .03em, width: 1em * 50%, height: 1em * 50%)

#enum(
  [ *Размытие по Гауссу*

  $ sigma = (N-1)/6 , "  " A_(i j) = exp( - ((i - (N+1)/2)^2 + (j -
    (N+1)/2)^2)/(2 sigma^2) ) $ 

  $ K_sigma = A/(sum_(i,j) A_(i,j)) $ ],

  [ *Блочное размытие*
  
  $ A_(i,j) = 1, "  " K_(#_rect) = A/(sum_(i,j)A_(i,j)) $ ],

  [ *Ядро увеличения резкости* 
  
  $ K_(*) = mat(delim: "[", 0, -1, 0; -1, 5, -1; 0, -1, 0) $ ],

  [ *Ядро выделения краёв* 

  $ K_(nabla) = mat(delim:"[", -1,-1,-1;-1,8,-1;-1,-1,-1) $ ],

  [*Ядро эффекта гравюры* 

  $ K_(arrow.l.r) = mat(delim: "[",
   1, 0, 0,  0, 0;
   0, 1, 0,  0, 0;
   0, 0, 0,  0, 0;
   0, 0, 0, -1, 0;
   0, 0, 0, 0, -1) $ ]
)

Размытие по Гауссу и Блочное размытие рассмотрим для трех различных
значений $N$: 7, 11, 17.

= Размытие по Гауссу

#for N in (7, 11, 17) [
#figure(grid(columns: 2, column-gutter: 1em,
  image(
    "../fig/task2/original_RGB.png"
  ),
  image(
    "../fig/task2/gaussian_{N}/gaussian_{N}_spatial_conv.png"
      .replace("{N}", str(N)),
  )),
  caption: [
    слева --- Исходное изображение
    Справа --- Результат после свертки с ядром Гауссового
    размытия ($N = #N$); ]
)
] 

Видим, как при увеличении N заметно усиливается размытие изображения.

Посмотрим на Фурье-образ изображения и каждого из ядер и на
произведение его на спектр изображения:
#figure(
  image(height: 10cm, 
    "../fig/task2/original_spectrum_RGB.png"
  ),
  caption: [Спектр исходного изображения]
)

#for N in (7, 11, 17) [
#figure(grid(columns: 2, column-gutter: 1em,
  image(height: 10cm, 
    "../fig/task2/gaussian_{N}/gaussian_{N}_kernel_spectrum.png"
      .replace("{N}", str(N))
  ),
  image(height: 10cm, 
    "../fig/task2/gaussian_{N}/gaussian_{N}_spectrum_after_spatial.png"
      .replace("{N}", str(N))
  )),
  caption: [
    Слева --- спектр ядра гауссового размытия (N = #N); \
    Справа --- произведение спектров ядра и изображения
  ]
)
]

Теперь поэлементно перемножим полученный спектр ядра и спектр
картинки. Для наглядности сразу разместим их рядом с результатом
свертки. Изображения полученные сверткой находятся справа, а
результаты произведения спектров ядра и изображения --- слева.

#for N in (7, 11, 17) [
#figure(grid(columns: 2, column-gutter: 1em,
  image(
    "../fig/task2/gaussian_{N}/gaussian_{N}_freq_filter.png"
      .replace("{N}", str(N))
  ),
  image(
    "../fig/task2/gaussian_{N}/gaussian_{N}_spatial_conv.png"
      .replace("{N}", str(N))
  )),
  caption: [
    Сравнение результатов свертки и умножения спектров для 
    гауссового размытия ($N = #N$)
  ]
)
]

Результат одинаковый.

= Блочное размытие

#for N in (7, 11, 17) [
#figure(grid(columns: 2, column-gutter: 1em,
  image(
    "../fig/task2/original_RGB.png"
      .replace("{N}", str(N))
  ),
  image(
    "../fig/task2/box_{N}/box_{N}_spatial_conv.png"
      .replace("{N}", str(N))
  )),
  caption: [
    Слева --- исходное изображение; \
    справа --- результат после свертки 
    с ядром блочного размытия ($N = #N$) ]
)
]

#for N in (7, 11, 17) [
#figure(grid(columns: 2, column-gutter: 1em,
  image(
    "../fig/task2/box_{N}/box_{N}_kernel_spectrum.png"
      .replace("{N}", str(N))
  ),
  image(
    "../fig/task2/box_{N}/box_{N}_spectrum_after_spatial.png"
      .replace("{N}", str(N))
  )
),
  caption: [
    Слева --- спектр ядра блочного размытия (N = #N); \
    Справа --- произведение спектров ядра блочного размытия и
    изображения ]
)] 

= Выделение краёв 

#let fig2img(img1, img2, caption: []) = {
  figure(grid(columns: 2, column-gutter: 1em, img1, img2),
  caption: caption)
} 

#figure(
  image("../fig/task2/edge_3/edge_3_spatial_conv.png", height: 10cm),
  caption: [ Результат свертки с ядром выделения краёв ]
)

#fig2img(
  image("../fig/task2/edge_3/edge_3_spatial_conv.png"),
  image("../fig/task2/edge_3/edge_3_freq_filter.png"),
  caption: [ Сравнение результатов свертки и умножения 
             спектров для ядра выделения краёв ]
)

#fig2img(
  image("../fig/task2/edge_3/edge_3_kernel_spectrum.png"),
  image("../fig/task2/edge_3/edge_3_spectrum_after_spatial.png"),
  caption: [
  Слева --- спектр ядра выделения краёв;  \
  Справа --- произведение спектров ядра выделения краёв и изображения ]
)


= Увеличение резкости 

#fig2img(
  image("../fig/task2/original_RGB.png"),
  image("../fig/task2/sharpen_3/sharpen_3_spatial_conv.png"),
  caption: [ Слева --- исходное изображение; \
             справа --- Результат свертки с ядром увеличения резкости ]
)

#fig2img(
  image("../fig/task2/sharpen_3/sharpen_3_spatial_conv.png"),
  image("../fig/task2/sharpen_3/sharpen_3_freq_filter.png"),
  caption: [ Сравнение результатов свертки и умножения 
             спектров для ядра увеличения резкости ]
)

#fig2img(
  image("../fig/task2/sharpen_3/sharpen_3_kernel_spectrum.png"),
  image("../fig/task2/sharpen_3/sharpen_3_spectrum_after_spatial.png"),
  caption: [
  Слева --- спектр ядра выделения краёв;  \
  Справа --- произведение спектров ядра увеличения резкости и изображения ]
)

= Эффект гравюры


#fig2img(
  image("../fig/task2/original_RGB.png"),
  image("../fig/task2/emboss_3/emboss_3_spatial_conv.png"),
  caption: [ Слева --- исходное изображение; \
             справа --- результат свертки с ядром эффекта гравюры ]
)

#fig2img(
  image("../fig/task2/emboss_3/emboss_3_spatial_conv.png"),
  image("../fig/task2/emboss_3/emboss_3_freq_filter.png"),
  caption: [ Сравнение результатов свертки и умножения 
             спектров для ядра увеличения резкости ]
)

#fig2img(
  image("../fig/task2/emboss_3/emboss_3_kernel_spectrum.png"),
  image("../fig/task2/emboss_3/emboss_3_spectrum_after_spatial.png"),
  caption: [ Слева --- спектр ядра выделения краёв;  \
             Справа --- произведение спектров ядра
             увеличения резкости и изображения ]
)

= Разница блочного и гауссового размытия

В то время как в спектрах изображений после гауссового и блочного
размытия различия видны сразу, не сразу понятно в чем отличие между
этими двумя ядрами, если смотреть только на результат свёртки.

Разместим изображения после блочного и гауссвого размытия бок о бок,
и попробуем выделить различия.

#let compfigsize = 45%
#figure(
    image(height: compfigsize,
    "../fig/task2/gaussian_17/gaussian_17_spatial_conv.png"),
    caption: [Результат гауссвого размытия ($N = 17$)]
)

#figure(
  image(height: compfigsize,
    "../fig/task2/box_17/box_17_spatial_conv.png"),
    caption: [Результат блочного размытия ($N = 17$)]
)

Сразу видно, что при одинаковом $N$ блочное размытие имеет более
заметный эффект. При более детальном рассмотрении можно увидеть как
блочное размытие при больших $N$ создает эффект "размытых пикселей";
интересно, что если всматриваться в изображание, глаза очень быстро устают.

Гауссово размытие же похоже на расфокусированный снимок или миопию.

= Выводы

Пронаблюдали за эффектом различных ядер свертки на цветном
изображении. Убедились в том, что теорема о свертке выполняется:
свертка изображения с ядром и обратное преобразование Фурье от
произведения спектров образа и изображения дают одинаковый результат.
Увидели разницу гауссового и блочного размытия, сравнив их между
собой: гауссово размытие дает естественный эффект размытия, а блочное
размытие добавляет артевакты, более заметные при увеличении $N$.
Заметили, что при увеличении $N$ усиливается эффект от ядер размытия.

// vim:set tw=70 sw=2 ts=4 :

