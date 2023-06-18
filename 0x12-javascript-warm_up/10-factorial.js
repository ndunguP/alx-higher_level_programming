#!/usr/bin/node
// Script that computes and prints a factorial
let factorial = function (num) {
  if (isNaN(Number(num))) {
    return (1);
  }
  return num ? num * factorial(num - 1) : 1;
};

let result = factorial(process.argv[2]);
console.log(result);
