function topla() {
    num1 = document.getElementById("firstnum").value;
    num2 = document.getElementById("secondnum").value;
    document.getElementById("result").innerHTML = Number(num1) + Number(num2);
}

function cix() {
    num1 = document.getElementById("firstnum").value;
    num2 = document.getElementById("secondnum").value;
    document.getElementById("result").innerHTML = num1 - num2;
}

function vur() {
    num1 = document.getElementById("firstnum").value;
    num2 = document.getElementById("secondnum").value;
    document.getElementById("result").innerHTML = num1 * num2;
}
document.querySelector('#vur').addEventListener('click',function(){
    document.querySelector('#result').style.backgroundColor='white';
})
document.querySelector('#topla').addEventListener('click',function(){
    document.querySelector('#result').style.backgroundColor='white';
})
document.querySelector('#cix').addEventListener('click',function(){
    document.querySelector('#result').style.backgroundColor='white';
})
document.querySelector('#bol').addEventListener('click',function(){
    document.querySelector('#result').style.backgroundColor='white';
})

function bol() {
    num1 = document.getElementById("firstnum").value;
    num2 = document.getElementById("secondnum").value;
    document.getElementById("result").innerHTML = num1 / num2;
}