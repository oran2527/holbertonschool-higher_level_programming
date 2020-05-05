#!/usr/bin/node
if (process.argv3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No arguments');
}
