let str = 'Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır';

// Number of characters
console.log('Number of characters : ' + str.length);

// Number of letters
let count = 0;
for (let i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) > 96 && str.charCodeAt(i) < 123) {
        count = count + 1;
    }
    if (str.charCodeAt(i) > 64 && str.charCodeAt(i) < 91) {
        count = count + 1;
    }
}
console.log('Number of Letters : ' + count);

// Collect all words
let words = str.split(" ");
console.log('All words : ' + words);

// Find words
let find = 'yox';
if (str.search(find) > 0) {
    console.log(find + ' - Verilmis cumlede tapildi!');
} else {
    console.log(find + ' - Verilmis cumlede yoxdur!');
}