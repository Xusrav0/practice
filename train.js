
// function reverseSentence(str){
//   const words = str.split(" ")
//   let newSentence = "";
  
//   for(let letter of words){
//     letter = letter.split("").reverse().join("")
//     newSentence = newSentence + " " + letter
//   }
//   return newSentence
// }
// const result = reverseSentence("we like coding");
// console.log(result)



/*  TASK L: 
Shunday function yozing, u string qabul qilsin va string ichidagi 
hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc";
*/

function reverseSentence(str) {
  return str.split(' ').map(word => word.split('').reverse().join('')).join(' ')

}


console.log(reverseSentence("we like coding!"))

// TASK K:
// Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
// MASALAN: countVowels("string") return 1;
/*
function countVowels(str) {
    let vowels = ["a", "e", "i", "o", "u", "y"];
    let count = 0;

    for (let char of str) {
        if (vowels.includes(char.toLowerCase())) {
            count++;
        }
    }

    return count;
}

console.log(countVowels("string"));
// console.log(countVowels("University"));


*/






// TASK G:

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.
/*
function getHighestIndex(array) {
  let b = 0;
  let index = 0
 for (let i = 0; i < array.length; i++) {
  if(array[i] > b) {
    b = array[i]
    index = i
  }
 }
 return index
}

console.log(getHighestIndex([5, 21, 12, 21 ,8]))
*/



// TASK - F
/*
Yagona string argumentga ega findDoublers nomli function tuzing
Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
true yokida false natija qaytarsin.

MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

*/
/*
function findDoublers(a) {
  let b = '';
for (let char of a) {
  if (b.includes(char)) {
    return true
  } 
  
  b += char
}
return false
}




console.log(findDoublers('hello'))
// console.log(findDoublers('Microsoft'))
// console.log(findDoublers('austin'))


*/





// TASK - E

/*
Shunday function tuzing, u bitta string argumentni qabul 
qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/
/*
function getReverse(a) {
  return a.split("").reverse().join("");
}

console.log(getReverse("hello"));
console.log(getReverse("transformers"));
*/