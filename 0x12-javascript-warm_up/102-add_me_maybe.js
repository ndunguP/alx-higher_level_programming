#!/usr/bin/node
let addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
exports.addMeMaybe = addMeMaybe;
