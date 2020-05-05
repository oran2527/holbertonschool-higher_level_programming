#!/usr/bin/node

let args = 0
let text1
let text2
process.argv.forEach((val, index) => {
  args += 1
  if (index === 2) {
    text1 = val    
  }
  if (index === 3) {
    text2 = val    
  }
});
console.log(text1 + ' is ' + text2)
