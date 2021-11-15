let soz = prompt('Sozu daxil edin: ');
for (let i = 0; i < soz.length; i++) {
    if (soz.charCodeAt(i) < 91 && soz.charCodeAt(i) > 64) {
        soz.replace(soz[i], soz[i].toLocaleLowerCase());
    }
    if (soz.charCodeAt(i) < 123 && soz.charCodeAt(i) > 96) {
        soz.replace(soz[i], soz[i].toLocaleUpperCase());
    }
}
console.log(soz)
