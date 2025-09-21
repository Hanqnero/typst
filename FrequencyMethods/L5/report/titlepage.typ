#let TitlePage(
  title,
  author, // (name, group, isu)
  uni // (university, faculty, city)

) = page(
  header: [
    #uni.university #h(1fr) #uni.faculty
    #line(length: 100%, stroke: (.07em))
  ],
  footer: [
    #align(center+top, [#uni.city, #datetime.today().year()])
  ],
)[
  #place(center+horizon, float:false, 
    text(size: 2em, title)
  )
  #place(end+horizon, dy: 20%)[
    Выполнил: #author.name --- #author.group \ 
    #author.isu
  ]
]