let arr1 = [1, 3, 5, 7, 9, 11]
let arr2 = [2, 4, 6, 8]
let len1 = arr1.length;
let len2 = arr2.length;

for (let i = 0; i < len2; i++) {
    arr1[i + len1] = arr2[i];
}
console.log(arr1);