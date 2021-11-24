let soz = prompt('Sozu daxil edin : ');
let newSoz='';
for (let i = 0; i < soz.length; i++) {
    if (soz.charCodeAt(i) < 91 && soz.charCodeAt(i) > 64) {
        newSoz+=soz[i].toLowerCase()
    }
    if (soz.charCodeAt(i) < 123 && soz.charCodeAt(i) > 96) {
        newSoz+=soz[i].toUpperCase()
    }
}
console.log(soz)
console.log(newSoz)