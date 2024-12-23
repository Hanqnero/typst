#import "style.typ": ReportStyle
#import "titlepage.typ": TitlePage

#import "@preview/codly:1.1.1"
#import "@preview/codly-languages:0.1.3"
#show: codly.codly-init.with()
#codly.codly(
  languages: codly-languages.codly-languages,
  zebra-fill: none,
)

#ReportStyle[

#TitlePage[
  Отчет по расчетно-графической работе №1 \ "Численное интегрирование дифференциальных уравнений первого порядка"
][ Смирнов Алексей Владимирович ][ 409578 ][ R3242 ]

= Вариант 16
Численно решить дифференциальное уравнение
$
  y'=y-x^2", "y(1) = 2
$
на отрезке $[0;2]$ с шагом $h=0.2$ методом Эйлера, модифицированным
методом Эйлера и методом Рунге-Кутта. Найти точное решение $y=y(x)$ и
сравнить значения точного и приближенных решений в точке $x=2$. 
Найти абсолютную и относительную погрешности в этой точке для каждого метода.
Вычисления вести с четырьмя десятичными знаками.

= Решение

#let lastListing = context counter(
  figure.where(kind: raw)).final().first()

Для численного решения уравнения удобно использовать средства языка программирования Python в совокупности с библиотекой NumPy. Для каждого из методов была написана программа, исходный код которых можно увидеть в Листингах 1--#lastListing.


== Метод Эйлера

#figure(
  include "table1.typ",
  caption: []
)

== модифицированный метод Эйлера
  
#figure(
  include "table2.typ",
  caption: []
)

== Метод Рунге-Кутта

#figure(
  include "table3.typ",
  caption: []
)

== Точное решение
Исходное уравнение
$
  y' = y - x^2
$
переносом $y$ в левую часть преобразуется в
линенейное неоднородное уравнение первого порядка.
$
  y' - y = -x^2
$

Характеристический многочлен
$
  lambda - 1
$

Решение соответствующего однородного уравнения
$
   lambda - 1 = 0 ==> lambda = 1 \
   y_0 = C_1 e^x
$

Подберем частное решение методом неопределенных коэффициентов. 
Правая часть
$
  -x^2
$
тогда частное решение имеет вид
$
  &tilde(y) = A x^2+B x+C \
  &tilde(y)' = 2A x + B \

  &tilde(y)' - tilde(y) = (-A)x^2 + (2A-B)x + (B-C) = -x^2
$
$
  cases(
    &&A = 1,
    2A-B &= 0 ==> &B = 2 ,
    B-C  &= 0 ==> &C = 2
  )
$
$
  tilde(y) = x^2 +2x + 2
$
Общее решение уравнения
$
  y = C_1 e^x +x^2+2x + 2
$

Начальные условия: $y(1) = 2$:
$
  2 = C_1 dot e + 1 + 2 + 2 \
  C_1 = -3/e
$
Финальное решение
$
  y(x) = -3/e e^x + x^2+2x+2 \
$

== Сравнение результатов

#figure(
  
  text(size: 0.9em, include "table4.typ"),
  caption: []
)




#figure(
```python
import numpy as np
np.set_printoptions(4)
XS = np.linspace(0,2,11)
I = np.where(XS == 1)[0][0]
n = N = XS.shape[0]
h = np.float64('.2')
f = lambda x,y: y - x*x
cellformat = lambda x: "[{:5.4f}]".format(x)

table1_i = np.array(range(1, n+1))
table1_x = XS
table1_y = np.zeros((n,), dtype=np.float64)
table1_y[I] = 2
table1_f = np.zeros((n,), dtype=np.float64)
table1_deltay = np.zeros((n,), dtype=np.float64)

for i in range(I, 0, -1):
    table1_f[i] = f(table1_x[i], table1_y[i])
    table1_deltay[i] = -h*table1_f[i]
    table1_y[i-1] = table1_y[i] + table1_deltay[i]
for i in range(I, N-1):
    table1_f[i] = f(table1_x[i], table1_y[i])
    table1_deltay[i] = h*table1_f[i]
    table1_y[i+1] = table1_y[i] + table1_deltay[i]

table1 = np.vstack((table1_i, table1_x, table1_y, table1_f, table1_deltay)).T
```,
caption: [Решение уравния методом Эйлера]
)

#figure(
```python
# ...

table2_i = np.arange(1, n+1)
table2_x = XS
table2_y = np.zeros((n,), dtype=np.float64)
table2_f = np.zeros((n,), dtype=np.float64)

table2_x2 = table2_x + h / 2
table2_y2 = np.zeros((n,), dtype=np.float64)
table2_f2 = np.zeros((n,), dtype=np.float64)

table2_deltay = np.zeros((n,), dtype=np.float64)

table2_y[I] = 2


for i in range(I, 0, -1):
    table2_f[i] = f(table2_x[i], table2_y[i])

    # table2_x2
    table2_y2[i] = table2_y[i] -h/2 * table2_f[i]
    table2_f2[i] = f(table2_x2[i], table2_y2[i])

    table2_deltay[i] = -h*table2_f2[i]
    table2_y[i-1] = table2_y[i] + table2_deltay[i]
 
for i in range(I, n-1):
    table2_f[i] = f(table2_x[i], table2_y[i])

    # table2_x2
    table2_y2[i] = table2_y[i] + h/2 * table2_f[i]
    table2_f2[i] = f(table2_x2[i], table2_y2[i])

    table2_deltay[i] = h*table2_f2[i]
    table2_y[i+1] = table2_y[i] + table2_deltay[i]

table2 = np.vstack((table2_i, 
                         table2_x, table2_x2, 
                         table2_y, table2_y2, 
                         table2_f, table2_f2, 
                         table2_deltay)).T
```,
  caption: [Решение уравнения модифицированным методом Эйлера]
)

#figure(
```python
# ...

table3_i  = np.arange(0, N)
table3_x1 = XS
table3_x2 = table3_x1 + h / 2 
table3_x3 = table3_x1 + h / 2
table3_x4 = table3_x1 + h

table3_y1 = np.zeros((n,),dtype=np.float64)
table3_y1[I] = 2

table3_y2 = np.zeros((n,),dtype=np.float64)
table3_y3 = np.zeros((n,),dtype=np.float64)
table3_y4 = np.zeros((n,),dtype=np.float64)

table3_K1 = np.zeros((n,),dtype=np.float64)
table3_K2 = np.zeros((n,),dtype=np.float64)
table3_K3 = np.zeros((n,),dtype=np.float64)
table3_K4 = np.zeros((n,),dtype=np.float64)

table3_Dy = np.zeros((n,),dtype=np.float64) 

for i in range(I, 0, -1):
    table3_K1[i] = f(table3_x1[i], table3_y1[i]) * -h

    table3_y2[i] = table3_y1[i] + table3_K1[i] / 2
    table3_K2[i] = f(table3_x2[i], table3_y2[i]) * -h

    table3_y3[i] = table3_y1[i] + table3_K2[i] / 2
    table3_K3[i] = f(table3_x3[i], table3_y3[i]) * -h

    table3_y4[i] = table3_y1[i] + table3_K3[i]
    table3_K4[i] = f(table3_x4[i], table3_y4[i]) * -h

    table3_Dy[i] = 1/6 * (table3_K1[i] + 2*table3_K2[i] + 
                          2*table3_K3[i] + table3_K4[i])
    
    table3_y1[i-1] = table3_y1[i] + table3_Dy[i]

for i in range(I, n-1):
    table3_K1[i] = f(table3_x1[i], table3_y1[i]) * h

    table3_y2[i] = table3_y1[i] + table3_K1[i] / 2
    table3_K2[i] = f(table3_x2[i], table3_y2[i]) * h

    table3_y3[i] = table3_y1[i] + table3_K2[i] / 2
    table3_K3[i] = f(table3_x3[i], table3_y3[i]) * h

    table3_y4[i] = table3_y1[i] + table3_K3[i]
    table3_K4[i] = f(table3_x4[i], table3_y4[i]) * h

    table3_Dy[i] = 1/6 * (table3_K1[i] + 2*table3_K2[i] + 
                          2*table3_K3[i] + table3_K4[i])
    
    table3_y1[i+1] = table3_y1[i] + table3_Dy[i]

table3 = np.vstack((table3_i, 
                    table3_x1, table3_x2, table3_x3, table3_x4, 
                    table3_y1, table3_y2, table3_y3, table3_y4, 
                    table3_K1, table3_K2, table3_K3, table3_K4, 
                    table3_Dy)).T
```,
caption: [Решение уравнения методом Рунге-Кутта]
)



]