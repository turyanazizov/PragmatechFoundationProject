let txt='web developer.'
let text=document.querySelector('#txt')
let i=0;
let len=txt.length

function write(){
    if(i<len){
        text.innerHTML+=txt.charAt(i);
        i++;
        setTimeout(write, 150);
    }
    else{
        text.innerHTML=''
        i=0
          write()
    }
}
write()
