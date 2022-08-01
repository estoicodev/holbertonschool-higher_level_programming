#!/usr/bin/node
const process = require('process');

if (process.argv.length >= 4) {
  let second = -Infinity;
  let highest = -Infinity;
  if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
    second = parseInt(process.argv[3]);
    highest = parseInt(process.argv[2]);
  } else {
    second = parseInt(process.argv[2]);
    highest = parseInt(process.argv[3]);
  }
  for (let i = 4; i < process.argv.length; i++) {
    const current = parseInt(process.argv[i]);
    if (current > second && current < highest) {
      second = current;
    }
    if (current > highest) {
      const tmp = highest;
      highest = current;
      second = tmp;
    }
  }
  console.log(second);
} else {
  console.log(0);
}
