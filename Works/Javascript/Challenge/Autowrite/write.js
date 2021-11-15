let txt='lorem ipsum doler sit comit'
let text=document.querySelector(".text")
let i=0;
let len=txt.length
function write(){
    if(i<len){
        text.innerHTML+=txt.charAt(i);
        i++;
        setTimeout(write, 100);
    }
    else{
        text.innerHTML=''
        i=0
          write()
    }
}
write()