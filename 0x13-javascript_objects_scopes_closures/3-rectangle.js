#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((typeof w === typeof h && typeof h === 'number') &&
    (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str = str + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}

module.exports = Rectangle;
