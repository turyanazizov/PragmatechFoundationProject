// Verilən 4 rəqəmli ədədin rəqəmlərinin cəmini tapan proqram yazın (Nümunə : let a=1298 Nəticə : 1+2+9+8=20)

let num = 1837;
let a;
let sum = 0;
for (let i = 0; i < 4; i++) {
    a = num % 10;
    sum = sum + a;
    num = Math.floor(num / 10);
}
console.log(sum);