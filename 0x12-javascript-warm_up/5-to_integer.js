#!/usr/bin/node

let args = 0
let num
process.argv.forEach((val, index) => {
  args += 1
  if (index === 2) {
    num = parseInt(val)    
  }  
});
if (args === 2) {
  console.log('Not a number')
}
if (args > 2 && num === num) {
  console.log('My number: ' + num)
}
if (args > 2 && num !== num) {
  console.log('Not a number')
}
