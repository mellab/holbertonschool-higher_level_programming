#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, el) => {
    if (el === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
