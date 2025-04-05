#let headerContent = [
  Университет ИТМО #h(1fr) ФСУиР
  #line(length:100%, stroke: (paint: black, thickness: .07em))
]

#let footerContent(year) = context [
  #h(1fr) #counter(page).display("1/1", both: true) #h(1fr)
]

#let ReportStyle(content) = {
  set page(
    paper: "a4",
    margin: 2cm,
    header: headerContent,
    footer: footerContent(datetime.today().year())
  )
  set par(
    justify: true,
    linebreaks: "optimized",
  )
  set text(
    lang: "ru",
    size: 14pt,
    font: ("New Computer Modern")
  )
  show figure: set block(breakable: true)

  set heading(numbering: "1.1.")

  content
}