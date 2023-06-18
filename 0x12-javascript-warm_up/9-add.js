#!/usr/bin/node
// Script that prints the addition of 2 integers
let add = function (a, b) {
  return (a + b);
};

let sum = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(sum);
