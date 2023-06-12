#!/usr/bin/node
let callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
exports.callMeMoby = callMeMoby;
