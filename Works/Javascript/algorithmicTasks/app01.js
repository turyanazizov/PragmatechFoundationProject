// let a=(3+4*2==2*3)&&(true+false/2) ifadəsinin nəticəsi nədir və səbəbini qeyd edin.

let a = (3 + 4 * 2 == 2 * 3) && (true + false / 2)

// ilk once and-in sol terefine baxilir burada 11 6-ya beraber olmadigi ucun false olur.
// Daha sonra false/2 false qiymet alir true ve false mentigi cemi de false qiymet alır.
// let a(false)&&(false) halina sadelesir.
// false 0-a beraberdir.and mentigi emeli ise vurma demekdir 0*0=0 yeni mentigi "false"  

console.log(a);