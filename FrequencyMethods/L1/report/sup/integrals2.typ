#let c_2n = [
  $
    c_(-2) = 1/8 integral_(-1)^7 f(t) e^(i pi/2 t) dif t = \
    1/8 [
      integral_(-1)^1 (2+2t i) e^(i pi/2 t) dif t +
      integral_1^3 ((4-2t) + 2i) e^(i pi/2 t) dif t +
      integral_3^5 (-2 +(8 - 2t)i) e^(i pi/2 t) dif t +
      integral_5^7 ((-12+2t) - 2i) e^(i pi/2 t) dif t 
    ] = \
    1/8 [
      (8(pi - 2))/pi^2 -
      (8i (-2 + pi))/pi^2 -
      (8 (-2 + π))/π^2 + 
      (8 i (-2 + π))/π^2 
    ] = 0
  $
]

#let _sum(exp_) = [
  $
    1/8 [
      integral_(-1)^1 (2+2t i) e^(#exp_) dif t +
      integral_1^3 ((4-2t) + 2i) e^(#exp_) dif t +
      integral_3^5 (-2 +(8 - 2t)i) e^(#exp_) dif t +
      integral_5^7 ((-12+2t) - 2i) e^(#exp_) dif t 
    ] 
  $
]

#let c_1n = [
  $
    c_(-1) = 1/8 integral_(-1)^7 f(t) e^(i pi/4 t) dif t = \
    #_sum($i pi/4 t$) = \
    1/8 [
      (16 sqrt(2) (-2 + π))/π^2 -
      (16 sqrt(2) (-2 + π))/π^2 + 
      (16 sqrt(2) (-2 + π))/π^2 -
      (16 sqrt(2) (-2 + π))/π^2
    ] = 0 
  $
]

#let c_0 = [
  $
    c_0 = 1/T integral_(-1)^7 f(t) dif t = \
    1/8 [
      integral_(-1)^1 2+2t i dif t + 
      integral_1^3 4-2t +2i dif t + 
      integral_3^5 -2 + (8-2t)i dif t + 
      integral_5^7 (-12+2t)-2i dif t
    ] = \ 1/8 [
      4 + -4i - 4 - 4i
    ] = 0
  $
]

#let c_1 = [
  $
    1/8 integral_(-1)^7 f(t) e^(-i pi/4 t) dif t = \
    1/8 [
        integral_(-1)^1 (2+2t i) e^(-i pi/4 t) dif t +
        integral_1^3 ((4-2t)+2i) e^(-i pi/4 t) dif t +
        integral_3^5 (-2+i(8-2t)) e^(-i pi/4 t) dif t +
        integral_5^7 ((-12+2t)-2i) e^(-i pi/4 t) dif t
    ] = \
    1/8 [
      (32 sqrt(2))/pi^2 + 
      (32 sqrt(2))/pi^2 +
      (32 sqrt(2))/pi^2 +
      (32 sqrt(2))/pi^2
    ] = 
    (16 sqrt(2))/pi^2
  $
]

#let c_2 = [
  $
    c_2 = 1/8 integral_(-1)^7 f(t) e^(-i pi/2 t) dif t = \
    1/8 [
      integral_(-1)^1 (2+2t i) e^(-i pi/2 t) dif t + 
      integral_(1)^3 (4-2t +2i) e^(-i pi/2 t) dif t + 
      integral_(3)^5 (-2+i(8-2t)) e^(-i pi/2 t) dif t + 
      integral_(5)^7 (-12+2t-2i) e^(-i pi/2 t) dif t + 
    ] = \
    1/8 [
      (8(2+pi))/pi^2 - 
      (8i(2+pi))/pi^2 -
      (8(2+pi))/pi^2 + 
      (8i(2+pi))/pi^2 
    ] = 0
  $
]