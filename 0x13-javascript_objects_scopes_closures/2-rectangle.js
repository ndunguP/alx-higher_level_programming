#!/usr/bin/node
/* Class that defines a Rectangle.
Initialize the instance attribute width with the value w
Initialize the instance attribute height with the value h
If w or h is equal to 0 or not a positive integer, create an empty object
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
