#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let str = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        if (i !== this.height - 1) {
          str += '\n';
        }
      }
      console.log(str);
    }
  }
}

module.exports = Square;
