#!/usr/bin/node
const process = require('process');

if (process.argv.length >= 3) {
  const n = parseInt(process.argv[2]);
  if (Number.isNaN(n)) {
    console.log('Missing size');
  } else {
    let str = '';
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        str += 'X';
      }
      if (i !== n - 1) {
        str += '\n';
      }
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
