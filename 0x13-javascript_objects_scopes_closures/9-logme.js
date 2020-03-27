#!/usr/bin/node
exports.logMe = (function (item) {
  let counter = 0;
  return function (item) {
    console.log(`${counter}: ${item}`);
    counter += 1;
  };
}());
