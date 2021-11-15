let num1 = prompt('1-ci eded: ');
let num2 = prompt('2-ci eded: ');
let count = 0;
if (num1 > 30 && num1 < 70) {
    count += 1;
}
if (num2 > 30 && num2 < 70) {
    count += 1;
}
if (count == 0) {
    console.log('Hec biri')
}
if (count == 1) {
    console.log('Yalniz biri')
}
if (count == 2) {
    console.log('Her ikisi')
}