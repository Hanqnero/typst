#import "titlepage.typ": TitlePage

#let ReportStyle(title, author, uni, body) = { 
  set text(
    size: 14pt,
    font: ("Times New Roman", "Helvetica"),
    lang: "ru"          
    )
  set par(
    justify: true,
    first-line-indent: (
      amount: 1em,
      all: true
    ),
    spacing: 1.5em,
  )
  set page(
    paper: "a4",
    margin: 2cm,
    header: [
      #uni.university #h(1fr) #uni.faculty
      #line(length: 100%, stroke: (.07em))
    ],
    footer: context align(center+horizon)[
      #counter(page).get().first() / #counter(page).final().first()
    ]
  )


  show heading: it => {
    set text(weight: "regular")
    if it.level <= 2 {
      set heading(numbering: "1.1.")
      set block(below: 1em)
      it
    } else {
      set heading(numbering: none, outlined: false)
      it
    }
  }


  show raw: it => {
    set align(left)
    set par(
      justify: false,
      spacing: 1em,
      first-line-indent: 0em,
    )
    set text(size: 11pt)

    block(width: 100%, breakable: true,
      it
    )
  }

  TitlePage(
    title,
    author,
    uni
  )

  page(footer: [])[
    #outline()
  ]
    
  counter(page).update(1)

  body
}
