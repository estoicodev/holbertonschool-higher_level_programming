#!/usr/bin/node
const process = require('process');

if (process.argv.length >= 3) {
  const n = parseInt(process.argv[2]);
  if (Number.isNaN(n)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
