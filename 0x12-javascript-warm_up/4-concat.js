#!/usr/bin/node
let text1;
let text2;
process.argv.forEach((val, index) => {
  if (index === 2) {
    text1 = val;
  }
  if (index === 3) {
    text2 = val;
  }
});
console.log(text1 + ' is ' + text2);
