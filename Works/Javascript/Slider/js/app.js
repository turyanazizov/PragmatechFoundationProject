let bigImage=document.querySelector('.big-img img')
function changeImage(elem){
    let imageSource=elem.getAttribute('src');
    bigImage.setAttribute('src',imageSource)
 }
