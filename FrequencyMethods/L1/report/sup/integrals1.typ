#let a0_solution = [
  $
    &a_0/2 = 1/T integral_(-T/2)^(T/2) f(x)dif x = 1/7 integral_(-3.5)^(3.5) f(x) dif x = \
    &= 1/7 (integral_(-3.5)^(0) 3 dif x + integral_(0)^(3.5) 5 dif x) = \
    &= 1/7 ( lr( ""/"" (3x)|)_(3.5)^(0) + lr(""/"" (5x)|)_(0)^(3.5) ) = \
    &= 1/7 ( 0 - (-(3 times 7)/2) + (5 times 7)/2 - 0) = 1/7 times (-7/2) times 8 = 4
  $
]
#let a1_solution = [
  #let intg = $integral$
  #let omegan = $2 pi n/T$
  $
    
    &a_1 = 2/T (intg_(-T/2)^(T/2) f(x) cos(omegan x) dif x)_cases(n = 1,T=7, delim: #none) =
    2/T (intg_(-T/2)^(T/2) f(x) cos(2pi 1/T x) dif x) = \
    &= 2/7 (intg_(-3.5)^(0) 3cos(2pi 1/7 x) dif x  + intg_(0)^(3.5) 5 cos(2pi 1/7 x) dif x ) = \
    &= 2/7[ 3 times 7/(2pi)  intg_(-3.5)^(0) cos (2pi 1/7 x) dif (2pi 1/7 x) + 
         5 times 7/(2pi) intg_(0)^(3.5) cos (2pi 1/7 x) dif (2pi 1/7 x)
    ] = \
    &= 21/(2pi) lr(sin((2pi x)/7)|)_(x=-3.5)^(x=0) + 35/(2pi) lr(sin((2pi x)/7)|)_(x=0)^(x=3.5) = \
    &= 21/(2pi)(sin(-pi) - sin(0)) + 35/(2pi)(sin(0) - sin(pi)) = 0

  $
]

#let a2_solution = [
  $
    &a_2 = 2/T lr((integral_(-T/2)^(T/2) f(x) cos(2pi n/T x) dif x))_(cases(n=2, T=7, delim: #none)) = 2/7 (integral_(-3.5)^(3.5) f(x) cos(4pi x/T) dif x) = \
    &= 2/7 [ integral_(-3.5)^(0) 3 cos(4pi x /7) dif x  + integral_(0)^(3.5) 5 cos(4pi x /7) dif x] = \
    &=  2/cancel(7) times 3 times cancel(7)/(4pi) lr(sin((4pi x)/7)|)_(-3.5)^(0) + 2/cancel(7) times 5 times cancel(7)/(4pi) lr(sin((4pi x)/7)|)_(0)^(3.5) = \
    &= 3/(2pi) (sin(-2pi) - sin(0)) + 5/(2pi)(sin(0)-sin(2pi)) = 0
  $
]

#let b1_solution = [
  $
    &b_1 = 2/T (integral_(-T/2)^(T/2) f(x) sin(2pi n/T x) dif x)_cases(delim: #none, n=1, T=7) = 2/T integral_(-7/2)^(7/2) f(x) sin(2pi x/7) dif x = \
    &= 2/T ( integral_(-7/2)^(0) 3 sin(2pi x/7) dif x + integral_(0)^(7/2) 5 sin(2pi x / 7) dif x ) = \
    &= 2/7 integral_(-7/2)^(0) 3 sin(2pi x / 7) 7/(2pi) dif ((2pi x )/7) + 2/7 integral_(0)^(7/2) 5 sin(2pi x / 7 ) (7)/(2pi) dif((2pi x)/7) = \
    &= lr(-(3 cos((2pi x) / 7))/pi |)_(-7/2)^(0) + lr(-(5 cos((2pi x) /7))/pi|)_(0)^(7/2) = [-(3cos 0 )/(pi) + (3cos(-pi))/pi] + [ -(5 cos(pi))/pi + (5cos 0)/pi] = \
    &= 3/pi [-1 + (-1)] + 5/pi [-(-1) + 1] = 10/pi - 6/pi = 4/pi
  $
]

#let b2_solution = [
  $
   & b_2 = 2/T (integral_(-T/2)^(T/2) f(x) sin(2pi n/T x) dif x)_cases(delim:#none, n=2, T=7) = 2/7 integral_(-7/2)^(7/2) f(x) sin(4pi/7 x) dif x = \
   &= 2/7 [ integral_(-7/2)^0 3 sin(4pi/7 x) dif x + integral_(0)^(7/2) 5 sin(4pi/7 x) dif x] = \
   &= 2/7 [ 
    (3times 7)/(4pi) integral_(-7/2)^0 sin(4pi/7 x) dif (4pi/7 x) + 
    (5 times 7)/(4pi) integral_(0)^(7/2) sin(4pi/7 x) dif (4pi / 7 x)
    ] = \
    &= 2/7 [ 
      -21/(4pi) lr(cos(4pi/7 x)|)_(-7/2)^(0) -
      35/(4pi) lr(cos(4pi/7 x)|)_(0)^(7/2)
    ] = \
    &= 2/7 [ -21/(4pi) underbrace((cos 0 - cos (-2pi)), 0) - 35/(4pi) underbrace((cos 2pi - cos 0 ), 0) ] = 0
  $
]

#let c1_solution = [
$ 
&c_1 = 
(1/T integral_(-T/2)^(T/2) f(x) e^(-i 2pi n/T x) dif x)_cases(T=7, n=1,
delim: #none) = 1/7 integral_(-7/2)^(7/2) f(x) e^(-i (2pi)/7 x) dif x = \
&= 
1/7 [ integral_(-7/2)^0 3 e^(-i (2pi)/7 x) dif x + 
integral_0^(7/2) 5 e^(-i (2pi)/7 x) dif x ] = \
&= 
1/7 [ 
(3 times 7)/(2pi) integral_(-7/2)^0 e^(-i (2pi)/7 x) dif ((2pi)/7x) + 
(5 times 7)/(2pi) integral_0^(-7/2) e^(-i (2pi)/7 x) dif ((2pi)/7x)
] = \
&= 
lr((3/(2pi) times (1/(-i)) e^(-i (2pi)/7 x))|)_(-7/2)^0 + 
lr((5/(2pi) times (1/(-i)) e^(-i (2pi)/7 x) )|)_0^(7/2) = \
&= 
(3i)/(2pi) (e^0 - e^(i pi)) + (5i)/(2pi) (e^(-i pi) - e^0) =
(3i)/(cancel(2)pi) times cancel(2) + (5i)/(cancel(2)pi) times (-cancel(2)) = \
&=
-(2i)/pi
$
]

#let c2_solution = [
$
  & c_2 = (1/T integral_(-T/2)^(T/2) f(x) e^(-i (4pi)/7 x) dif x)_cases(delim: #none, T=7, n=2) = 1/7 integral_(-7/2)^(7/2) f(x) e^(-i (4pi)/7 x ) dif x = \
  &= 
  1/7 [ integral_(-7/2)^0 3 e^(-i (4pi)/7 x ) dif x + integral_(0)^(7/2) 5 e^(-i (4pi)/7 x) dif x ] = \
  &=
  1/cancel(7) [ 
  (3 times cancel(7))/(-4pi i) integral_(-7/2)^0 e^(-i (4pi)/7 x) dif (-i (4pi)/7 x) +
  (5 times cancel(7))/(-4pi i) integral_(0)^(7/2) e^(-i (4pi)/7 x) dif (-i (4pi)/7 x)
  ] = \
  &=
  (3i)/(4pi) lr(""/"" e^(-i (4pi)/7 x)|)_(-7/2)^0 + (5i)/(4pi) lr( ""/""  e^(-i (4pi)/7 x)|)_0^(7/2) = (3i)/(4pi) (e^0 - e^(2pi i)) + (5i)/(4pi) (e^(-2pi i) - e^0) = 0
$
]
