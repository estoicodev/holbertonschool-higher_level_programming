#!/usr/bin/node
const process = require('process');

if (process.argv.length >= 3) {
  const n = parseInt(process.argv[2]);
  if (Number.isNaN(n)) {
    console.log('Not a number');
  } else {
    console.log(n);
  }
} else {
  console.log('Not a number');
}
