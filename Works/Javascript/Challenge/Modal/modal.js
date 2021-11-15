let body=document.querySelector("body")
let modal=document.querySelector(".modal")
let button=document.querySelector("button")
function openModal(){
    body.style.backgroundColor='gray'
    modal.style.display='flex'
    button.style.display='none'
}
function closeModal(){
    body.style.backgroundColor='white'
    modal.style.display='none'
    button.style.display='block'
}