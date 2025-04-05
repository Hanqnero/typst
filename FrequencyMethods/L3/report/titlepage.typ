#let footerContent(year) = [
#h(1fr) Санкт-Петербург, #year г. #h(1fr)
]

#let TitlePage(
  title, 
  author, 
  id, 
  studygroup
) = [

  #page(
    footer: footerContent(datetime.today().year())
  )[
    Автор: #author #h(1fr)
    ИСУ: #id #h(1fr)
    Группа: #studygroup #h(1fr)
    #{
      set text(weight: "bold", size: 1.5em)
      place(center+horizon, title)
    }

  ]

  #pagebreak()
  #counter(page).update(1)
]

#let OutlinePage(d: 3) = {
  page(numbering: "I", 
    outline(depth: d))
  pagebreak()
  counter(page).update(1)
}

// Preview title page
#import "style.typ": ReportStyle
#ReportStyle[
  #TitlePage(lorem(10))[Смирнов Алексей Владимирович][409578][R3242]
  #OutlinePage()
]
