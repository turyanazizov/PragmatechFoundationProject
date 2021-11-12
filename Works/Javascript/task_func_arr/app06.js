// Qrupunuzda olan tələbələrin yaşlarını bir array halına gətirin.
// Bu arraydan istifadə edərək tələbə yaşlarının 2 qatının olduğu yeni array yaradan funksiya yazın.

let arr = [20, 22, 30, 19];
let newArr = arr.map(foo);

function foo(num) {
    return num * 2;
}
console.log(newArr);