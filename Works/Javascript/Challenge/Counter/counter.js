let num=prompt('Enter a Number...');
n=num;
document.querySelector('.number').innerHTML=num;
Number(num)
function increase(){
    num=Number(num)+1;
    document.querySelector('.number').innerHTML=num;
}
function decrease(){
    num=Number(num)-1;
    document.querySelector('.number').innerHTML=num;
}
function reset(){
    num=Number(n);
    document.querySelector('.number').innerHTML=num;
}