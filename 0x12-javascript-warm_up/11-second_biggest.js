#!/usr/bin/node
const ar = [];
let ind = 0;
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  process.argv.forEach(function (val, index) {
    if (index > 1) {
      ar[ind] = process.argv[index];
      ind += 1;
    }
  });
  ar.sort(function (a, b) {
    return a - b;
  });
  console.log(ar[ar.length - 2]);
}
