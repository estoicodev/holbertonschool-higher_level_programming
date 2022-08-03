#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  if (!(dict[key] in newDict)) {
    newDict[dict[key]] = [key];
  } else {
    const newArray = newDict[dict[key]];
    newArray.push(key);
    newDict[dict[key]] = newArray;
  }
}

console.log(newDict);
