#!/usr/bin/node
// Script that prints My number: <num> if the first argument can be converted to an integer
if (!isNaN(Number(process.argv[2]))) {
  console.log('My number: ' + Number(process.argv[2]));
} else {
  console.log('Not a number');
}
