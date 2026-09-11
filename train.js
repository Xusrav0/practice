// TASK - F
/*
Yagona string argumentga ega findDoublers nomli function tuzing
Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
true yokida false natija qaytarsin.

MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

*/
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