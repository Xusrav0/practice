// TASK - E

/*
Shunday function tuzing, u bitta string argumentni qabul 
qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/

function getReverse(a) {
  return a.split("").reverse().join("");
}

console.log(getReverse("hello"));
console.log(getReverse("transformers"));
