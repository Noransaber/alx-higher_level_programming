#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
};
