#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (isNaN(width) || isNaN(height) || width <= 0 || height <= 0) {
      return;
    }
    this.width = width;
    this.height = height;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
