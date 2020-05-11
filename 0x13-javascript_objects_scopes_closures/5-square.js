#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    if (size > 0) {
      super();
      super.width = size;
      super.height = size;
    }
  }
}
module.exports = Square;
