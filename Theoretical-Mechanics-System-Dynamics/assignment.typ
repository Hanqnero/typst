#import "style.typ": ReportStyle
#set math.equation(numbering: "(1)")
#show ref: it => {
  let el = it.element
  
  if el.func() == math.equation {
    link(
      it.element.location(), 
      numbering(el.numbering,
      ..counter(math.equation).at(el.location())
    ))
  } else {
    it
  }
}

#ReportStyle[
  Вариант №3 #h(1fr) Смирнов Алексей Владимирович R3242

  #grid(
    align: top+left, 
    columns: 2, rows: 1,
    column-gutter: 1fr 
  )[
    == Дано
    $m_1$, $m_2$, $m_3$ \
    $R_1$, $i_1$ \
    $r_2$, $R_2$, $i_2$ \
    $M = italic("const")$\
    $M_C = italic("const")$ \
    $T_0 = 0$ \
    $s$ \
    $v_3$ --- ?
  ][
    #image("task.png")
  ]

  == Решение
  Напишем теорему об изменении кинетическо энергии:
  $
    T - underbrace(T_0, =0) = sum_(k=1)^n A^"внеш"_k
  $ <e0>
  Распишем кинетическую энергию системы в конечный момент времени
  $
    T = T_1 + T_2 + T_3 = (I_1 omega_1^2)/2 + (I_2 omega_2^2)/2 + (m_3 v_3^2)/2
  $ <e1>
  где
  $
    I_1 = m_1 i_1^2 \
    I_2 = m_2 i_2^2 \
  $

  Выражая $omega_1$ и $omega_2$ через $v_3$:
  $
    cases(omega_1 R_1 = omega_2 r_2,
    omega_2 R_2 = v_3)
    ==>
    cases(delim: #none, 
      omega_2 = v_3/R_2,
      omega_1 = omega_2 r_2 / R_1 = (v_3 r_2) / (R_1 R_2)
    )
  $
  Подставим в выражение @e1 для $T$
  $
    T = 1/2 v_3 underbrace([((i_1r_2)/(R_1 R_2))^2 + (i_2/R_2)^2 + m_3], "Приведенная масса системы "m_"пр")
  $

  Рассмотрим работы сил системы
  $
    sum_(k=1)^n A_k ^ "внеш" = A(M) + A(M_c) + A(m_3 g) = 
    M phi_1 - M_c phi_2 - m_3g s
  $ <e2>
  
  Выражая $phi_1$ и $phi_2$ через $s$:
  $
    &omega_1 = (r_2 v_3) / (R_1 R_2) = dot(phi_1) ==> 
    phi_1 = integral r_2/(R_1 R_2) underbrace(v_3 dif t, dif s) = 
    (r_2 s )/(R_1 R_2) \

    &omega_2 = dot(phi_2) ==> phi_2 = s/R_1 \
  $

  подставим в @e2
  $
    A = underbrace([M r_2/(R_1 R_2) - M_c 1/R_2 - m_3g ],
    "приведенная сила системы " Q_"пр") s
  $

  Подставим приведенные массу и силу системы в @e0 
  $
    1/2 m_"пр" v_3 ^2 = Q_"пр" s
  $
  Отсюда
  $
    v_3 = sqrt((2 Q_"пр" s)/m_"пр") = 
    sqrt((2 s (M r_2/(R_1 R_2) - M_c (1)/R_2 - m_3 g ))
    /
    (((i_1r_2)/(R_1 R_2))^2 + (i_2/R_2)^2 + m_3))
  $
  == Ответ
  $
    v_3 = 
    sqrt((2 s (M r_2/(R_1 R_2) - M_c (1)/R_2 - m_3 g ))
    /
    (((i_1r_2)/(R_1 R_2))^2 + (i_2/R_2)^2 + m_3))
  $
  
  
]