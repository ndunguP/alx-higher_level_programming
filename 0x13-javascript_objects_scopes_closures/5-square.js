#!/usr/bin/node
/* Class Square that inherits from Rectangle
*/
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
