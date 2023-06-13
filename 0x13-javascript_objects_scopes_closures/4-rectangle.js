#!/usr/bin/node
/* Class that defines a Rectangle.
Initialize the instance attribute width with the value w
Initialize the instance attribute height with the value h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using
the character X
Create an instance method rotate) tat exchanges the width and the height
of the rectangle
Create an instance method called double() that multiplies the width and
the height of the rectangle by 2
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let s = 'X';
    s = s.repeat(this.width) + '\n';
    s = s.repeat(this.height).slice(0, -1);
    console.log(s);
  }
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
