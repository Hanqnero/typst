#import "style.typ": ReportStyle

#set heading(numbering: "1.1")
#set figure.caption(separator: [ --- ])
#show figure.where(kind: image): set figure(supplement: "Рисунок")
#set math.equation(numbering: "(1)") 


#show: ReportStyle.with(
  [Лабораторная работа № 6. \ Обработка изображений],
  (
    name: [Смирнов Алексей Владимирович],
    group: [R3242],
    isu: [409578]
  ),
  (
    university: [Университет ИТМО],
    city: [г. Санкт-Петербург],
    faculty: [Факультет СУиР]
  )
)

= Задание 1
#[
  #set heading(offset: 1)
  #include "Task1.typ"
]

= Задание 2
#[
  #set heading(offset: 1)
  #include "Task2.typ"
]


// vim:set noai tw=70 wm=10 sw=2 ts=4 :
