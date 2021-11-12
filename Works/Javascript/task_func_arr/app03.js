// il dəyəri daxil edildiyi zaman onun necə ay və necə gün olduğunu return edən funksiya yazın
let il=prompt("Il deyeri daxil edin :");

function hesabla(year){
    year=il;
    ay=year*12;
    gun=year*365;
    return{
        ay,
        gun
    };
}
console.log(hesabla());