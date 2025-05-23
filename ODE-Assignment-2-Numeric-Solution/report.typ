#import "style.typ": ReportStyle
#import "titlepage.typ": TitlePage

#ReportStyle[

#TitlePage[
Отчет по расчетно-графической работе №2 \ "Численное интегрирование дифференциальных уравнений второго порядка"
][ Смирнов Алексей Владимирович ][ 409578 ][ R3242 ]
= Вариант 16
Методом Рунге-Кутта проинтегрировать дифференциальное уравнение
$
  y'' = 2y + x e^(-x)
$
на отрезке $[0, 0.3]$ с шагом $h = 0.1$.
Найти аналитическое решение уравнения
$y = y(x)$ и сравнить значение точного и приближенного решений в точках$x_1 = 1$, $x_2 = 2$, $x_3 = 3$. 
Все вычисления вести с шестью десятичными знаками.

== Численное решение
Понизим порядок уравнения превратив его в систему
$
  cases(
    y' = z,
    z' = 2y + x e ^ (-x)
  )\
$
Пусть 
$
  & g(x,y) = 2y + x e ^ (-x) \
  & f(z)   = z 
$

Одна итерация метода Рунге-Кутта
$
  cases(
  y_(i+1) = y_i+Delta y_i,
  z_(i+1) = z_i + Delta z_i
  )
$

$
  Delta z_i = 1/6 (K^((i))_1 + 2 K^((i))_2 + 2 K^((i))_3 + K^((i))_4) \
  Delta y_i = 1/6 (l^((i))_1 + 2 l^((i))_2 + 2 l^((i))_3 + l^((i))_4)
$

$
  x_0 = 0 \
  y_0 = y(0) = 2 \
  z_0 = y'(0) = 1 \
$

#let K0 = $K^((0))$
#let l0 = $l^((0))$
$
  K0_1 = h g(x_0, y_0) =  0.4 \
  l0_1 = h f(z_0) = 0.1 \ 
$
$
  K0_2 = h g( x_0 + h / 2, y_0 + l0_1 / 2) = 0.414756 \
  l0_2 = h f(z_0 + K0_1 / 2) = 0.120000 \ 
$
$
  K0_3 = h g( x_0 + h / 2, y_0 + l0_2 / 2) = 0.416756 \
  l0_3 = h f(z_0 + K0_2 / 2) = 0.120738 \
$
$
  K0_4 = h g(x_0 + h, y_0 + l0_3 / 2) = 0.421122 \
  l0_4 = h f(z_0 + K0_3 / 2) = 0.120838 \
$
$

  Delta y_0 = 0.702313", "Delta z_0 = 2.484147
$
Все вычисления для каждой итерации представлены в @t1[Таблице].

#figure(
  caption: figure.caption(position: top)[Результаты вычислений численного решения уравнения],
  include "table1.typ",
) <t1>

== Аналитическое решение
Линейное неоднородное уравнение второго порядка
$
  y'' = 2y + x e^x
$
  
$
  y'' - y = x e^x
$
Решение соответствующего однородного уравнения
$
  lambda^2 - 2lambda = 0 \
  lambda_(1,2) = plus.minus sqrt(2)
$
$
  y_0 = C_1 e^(sqrt(2) x) + C_2 e^(-sqrt(2) x)
$
Подбор частного решения по виду правой части
$
  tilde(y)   & = (A x + B) & e ^ (-x) \
  tilde(y)'  & = (A - B - A x) & e^ (-x) \
  tilde(y)'' & = (-2A + B + A x) & e ^ (-x) \
$

$
  tilde(y)'' - 2 tilde(y) = e^(-x) (-A x -2A - B) = x e ^ (-x) \
  cases(
    -A x &= x,
    -2A - B &= 0
  ) 
  ==>
  cases(
    A = -1,
    B = 2
  )
$

Общее решение уравнение

$
  y(x) = C_2 e^(sqrt(2) x) + C_1 e^(-sqrt(2) x) + (2 - x) e^(-x)
$

Начальные условия: $y(0) = 2$, $y'(0) = 1$

$
  cases(
    1 = -sqrt(2) C_1 + sqrt(2) C_2 - 1 - 2,
    2 = C_1 + C_2 + 2
  ) ==>
  cases(
    C_1 = -C_2,
    -sqrt(2)C_1 + sqrt(2)C_2 = 2
  ) \

  2sqrt(2)C_2 = 2 ==> C_2 = 1/sqrt(2)\
  
  cases(
    C_2 =   & 1/sqrt(2),
    C_1 = - & 1/sqrt(2)
  )
$

  Финальное решение
$
  y(x) = -1/sqrt(2) e^(-sqrt(2) x) + 1/sqrt(2) e^(sqrt(2) x) 
  + (2-x) e^(-x)
$

== Сравнение результатов
Представлены в @t2[Таблице].

#figure(
  include "table2.typ",
  caption: figure.caption(position:top)[Сравнение численного и аналитического решения]
) <t2>
] 
