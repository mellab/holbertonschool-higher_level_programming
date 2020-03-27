#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((arr, el) => {
    arr.unshift(el);
    return arr;
  }, []);
};
