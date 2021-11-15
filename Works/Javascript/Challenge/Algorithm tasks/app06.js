let colors=['red','yellow']
let addColor=prompt('Elave olunacaq reng sayini yazin: ')

for(let i=0;i<addColor;i++){
    newColor=prompt('Yeni reng eleva edin: ');
    colors.push(newColor);
}

console.log(colors)