let body=document.querySelector("body")
let arr=['blue','red','green']
let text=document.querySelector(".changeButton")
let i=0
function change(){
    body.style.background=arr[i]
    text.innerHTML=arr[i]
    i++;
    if(i==3){
        i=i-3;
    }
}
