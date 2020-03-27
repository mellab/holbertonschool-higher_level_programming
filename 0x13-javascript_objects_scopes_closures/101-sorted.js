#!/usr/bin/node

const { dict } = require('./101-data');

console.log(Object.entries(dict).reduce((d, el) => {
  !d[el[1]]
    ? d[el[1]] = [el[0]]
    : d[el[1]].push(el[0]);
  return d;
}, {}));
