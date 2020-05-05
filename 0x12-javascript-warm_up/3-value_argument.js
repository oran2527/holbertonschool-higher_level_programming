#!/usr/bin/node

let args = 0;
let text = '';
process.argv.forEach((val, index) => {
  args += 1;
  if (index === 2) {
    text = val;
  }
});
if (args === 2) {
  console.log('No argument');
}
if (args > 2) {
  console.log(text);
}
