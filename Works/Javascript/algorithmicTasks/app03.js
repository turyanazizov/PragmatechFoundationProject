// Verilən ədədin rəqəmləri arasında olan tək rəqəmləri ekranda göstərən proqram yazın (Nümunə : let a=1298 Nəticə : 1,9)

let num = 1426;
let a;
for (let i = 0; i < 4; i++) {
    a = num % 10;
    num = Math.floor(num / 10);
    if (a % 2 == 1) {
        console.log(a);
    }
}