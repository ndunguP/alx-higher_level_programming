#!/usr/bin/node
// Script that prints a message depending on the number of arguments passed
if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv[2]) {
  console.log(process.argv[2]);
}
