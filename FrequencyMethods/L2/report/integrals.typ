#set page(paper: "a4", margin: 2cm)
#set text(size: 14pt)

#let oo = $infinity$
#let dt = $dif t$
#let Bar = $lr(()/()|)$
#let om = $omega$

#let squarefunc_image = $
  1/sqrt(2pi) integral_(-oo)^(oo) f(t) e^(-i om t) dt = 
  1/sqrt(2pi) integral_(-b)^(b) a e^(-i om t) dt = 
  a/sqrt(2pi) integral_(-b)^(b) e^(-i om t) dt = \

  = a/sqrt(2pi)  integral_(-b)^b e^(-i om t) 1/(-i om) dif (-i om t) = \ 

  = a/sqrt(2pi) times 1/(-i om) e^(-i om t ) Bar_(t=-b)^(t=b) = 
  a/sqrt(2pi) times (e^(-i om b) - e^(i om b))/(-i om) = \

  = a/sqrt(2pi) times (cancel(cos om b) - i sin om b - cancel(cos om b) - i sin om b)/(-i om) = \

  = a/sqrt(2pi) times (cancel(-i) 2sin om b)/(cancel(-i) om) = 
  (2a)/sqrt(2pi) (sin om b) / om = (2a b)/sqrt(2pi) sinc om b = \
  = (sqrt(2) a b) / sqrt(pi) sinc om b
$

#let gr = text.with(fill:green)
#let re = text.with(fill:red)
#let c(n) = $#circle(radius:7pt, align(center+horizon, n))$

#let triang_imag = $
  hat(f)(t) = 1/sqrt(2pi) integral_(-oo)^oo f(t) e^(-i om t) dt \
  integral_(-oo)^oo f(t) e^(-i om t) dt = 
  gr(integral_(-b)^0 (a + a/b t) e^(-i om t) dt) +
  re(integral_(0)^b (a- a/b t) e^(-i om t) dt) = #c[I] \
  

  //=====
  //FIRST
  //=====
  gr(integral_(-b)^0 (a+a/b t) e^(-i om t) dt) = 
  mat(delim:"|",
    u = a+a/b t, dif &u = a/b dt;
    dif v = e^(-i om t) dt, &v = e^(-i om t)/(-i om)
  ) = \

  = (a + a/b t) lr((e^(-i om t) / (-i om)) |)_(t=-b)^(t=0) -
    integral_(-b)^0 (e^(-i om t)/(-i om)) a/b dt = \
  
  = lr((a i)/om - (a cancel(i))/(-cancel(i) om^2 b) e^(-i om t) |)_(t=-b)^(t=0) =
  (a i)/om + a/(b om^2)(1-e^(i om b)) \

  // ======
  // SECOND
  // ======
  re(integral_0^b (a- a/b t)e^(-i om t) dt) = 
  mat(delim:"|",
    u = a-a/b t, dif &u = -a/b dt;
    dif v = e^(-i om t) dt, &v = e^(-i om t)/(-i om)
  ) = \

  = (a - a/b t) lr((e^(-i om t) / (-i om)) |)_(t=0)^(t=b) -
    integral_0^b (e^(-i om t)/(-i om)) (-a/b) dt = \
  
  = -(a i)/om + (a cancel(i)) / (om b) times 1/(-cancel(i) om)  e^(-i om t) Bar_(t=0)^(t=b) =
  -(a i)/om - a/(b om^2)(e^(i om b) - 1) \

  #c[I] = cancel((a i)/om) - cancel((a i)/om) + 
  a/(b om^2) - (a e^(i om b))/(b om^2) + a/(b om^2) - (a e^(-i om b))/(b om^2) = \

   =(2 a)/(b om^2)(1 - [e^(i om b) + e^(-i om b)]) = (2a)/(b om^2)(1 - 2cos om b) \

   hat(f)(om) = 2/sqrt(2pi) (2a)/(b om^2)(1 - 2cos om b)


$

#let last_imag = $
  hat(f)(om) = 2/sqrt(2pi) integral_(-oo)^oo a e^(b|t|) e^(-i om t) dt \

  integral_(-oo)^oo a e^(b|t|) e^(-i om t) dt = 
  gr(integral_(-oo)^0 a e^(b t) e^(-i om t) dt) + 
  re(integral_0^oo a e^(-b t) e^(-i om t) dt) = #c[II] \

  gr(integral_(-oo)^0 a e^(b t) e^(-i om t) dt) = 
  a integral_(-oo)^0 e^((b-i om) t)dt = (a e^(b - i om t))/(b - i om) = a/(b - i om) \

  re(integral_0^oo a e^(-b t) e^(-i om t) dt) = 
  a integral_0^(oo) e^((-b -i om) t) dt = (a e^((-b - i om )t))/(-b - i om) = a/(b + i om) \

  #c[II] = a/(b - i om) + a/(b + i om) = (2 a b)/(b^2-om^2) \ 

  hat(f)(om) = 1/sqrt(2pi) (2 a b)/(b^2-om^2)
$