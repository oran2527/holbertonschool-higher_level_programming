#!/usr/bin/node
let res = 1
function fac (res, arg) {
  if (arg > 1) {
    res *= arg;
    fac (res, arg - 1);
  }
  else {
    console.log(res);
  };
};
fac (res, parseInt(process.argv[2]));
