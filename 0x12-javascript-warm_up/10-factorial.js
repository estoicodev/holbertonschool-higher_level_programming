#!/usr/bin/node
const process = require('process');

function factorial(n) {
  if (Number.isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (process.argv.length >= 3) {
  const n = parseInt(process.argv[2]);
  console.log(factorial(n));
} else {
  console.log(factorial(NaN));
}
