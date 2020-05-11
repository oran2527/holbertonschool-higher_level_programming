#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c) {
    let text = '';
    if (c === undefined) {
      text = 'X';
    } else {
      text = c;
    }
    for (let i = 0; i < this.height; i++) {
      let conc = '';
      for (let j = 0; j < this.width; j++) {
        conc += text;
      }
      console.log(conc);
    }
  }

  rotate () {
    const cw = this.width;
    const ch = this.height;
    this.width = ch;
    this.height = cw;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
