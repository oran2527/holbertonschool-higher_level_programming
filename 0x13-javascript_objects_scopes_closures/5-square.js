#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.width = size;
    this.height = size;
  }
}
module.exports = Square;
