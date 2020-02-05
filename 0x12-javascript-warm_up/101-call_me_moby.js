#!/usr/bin/node

exports.callMeMoby = (num, func) => {
  for (let i = 0; i < num; i++) {
    func();
  }
};
