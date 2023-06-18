#!/usr/bin/node
// Script that prints x times “C is fun”
if (!process.argv[2] || isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
}
for (let size = 0; size < process.argv[2]; size++) {
  console.log('X'.repeat(process.argv[2]));
}
