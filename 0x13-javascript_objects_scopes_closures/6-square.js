#!/usr/bin/node
/* Class Square that inherits from Rectangle
Create and instance method called charPrint(c) that
prints the rectangle using the character c.
If c is undefined, the the character X
*/
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    c = c.repeat(this.width) + '\n';
    c = c.repeat(this.height).slice(0, -1);
    console.log(c);
  }
};
