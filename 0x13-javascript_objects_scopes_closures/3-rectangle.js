#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      if (i !== this.height - 1) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Rectangle;
