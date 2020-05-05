#!/usr/bin/node
let args = 0;
process.argv.forEach(() => {
  args += 1;
});
if (args === 2) {
  console.log('No argument');
}
if (args === 3) {
  console.log('Argument found');
}
if (args > 3) {
  console.log('Arguments found');
}

