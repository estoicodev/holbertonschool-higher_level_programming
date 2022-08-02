#!/usr/bin/node
const functions = {
  nbOccurences: function (list, target) {
    let occurrences = 0;
    for (const item of list) {
      if (item === target) {
        occurrences++;
      }
    }
    return occurrences;
  }
};

module.exports = functions;
