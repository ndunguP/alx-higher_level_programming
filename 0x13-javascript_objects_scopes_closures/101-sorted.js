#!/usr/bin/node
/* Script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence */
const dict = require('./101-data.js').dict;
const newDict = {};
for (let val in dict) {
  if (dict[val] in newDict) {
    newDict[dict[val]].push(val);
  } else {
    newDict[dict[val]] = [val];
  }
}
console.log(newDict);
