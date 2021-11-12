// Prompt metodu vasitəsi ilə istifadəçinin yaşını daxil etməsini istəyin.
// - İstifadəçinin yaşı 30-dan kiçikdirsə istifadəçinin yaşının kvadratını ekrana çap edin
// - Yaş 30-40 aralığındadırsa daxil edilən ədədin son rəqəmini ekrana çap edin
// - Yaş 0-dan kiçik vəya 100-dən böyükdürsə ekrana "Düzgün məlumat daxil etməmisiniz" yazdırın

let yas = prompt("Yasinizi daxil edin :");
if (yas < 30 && yas > 0) {
    console.log(yas * yas);
}
if (yas > 30 && yas < 40) {
    console.log(yas % 10);
}
if (yas < 0 || yas > 100) {
    console.log("Düzgün məlumat daxil etməmisiniz");
}