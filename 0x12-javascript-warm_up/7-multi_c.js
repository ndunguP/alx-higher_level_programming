#!/usr/bin/node
// Script that prints x times “C is fun”
if (!process.argv[2] || isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log('C is fun');
}
