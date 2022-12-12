#!/usr/bin/node
const counter = function () {
  let count = 0;
  return function (item) {
    console.log(`${count}: ${item}`);
    return ++count;
  };
};

exports.logMe = counter();
