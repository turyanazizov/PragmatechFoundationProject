let soz = 'SaLaMhG';
for (let i = 0; i < soz.length; i++) {
    if (soz.charCodeAt(i) < 91 && soz.charCodeAt(i) > 64) {
        soz = soz.replace(soz[i], 'soz.toLocaleLowerCase(i)');
    }
    if (soz.charCodeAt(i) < 123 && soz.charCodeAt(i) > 96) {
        soz = soz.replace(soz[i], 'soz.toLocaleUpperCase(i)');
    }
}