#!/usr/bin/node
const process = require('process');

if (process.argv.length < 3 || Number.isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(process.argv[2]);
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
