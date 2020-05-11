#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      this.print(c);
    }
  }
}
module.exports = Square;
