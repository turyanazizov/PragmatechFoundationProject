let obj = {
    ad: 'Turyan',
    soyad: 'Azizov',
    yas: '21',
    olke: 'Azerbaycan'
}

let keys = Object.keys(obj);

for (let i = 0; i < keys.length; i++) {
  console.log(obj[keys[i]]);
}