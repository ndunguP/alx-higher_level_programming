#!/usr/bin/node
/* Script that imports an array and computes a new array */
const aList = require('./100-data.js').list;
let i = 0;
const newList = aList.map(function (num) {
  return num * i++;
});
console.log(aList);
console.log(newList);
