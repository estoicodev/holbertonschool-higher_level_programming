#!/usr/bin/node
const process = require('process');

let isEmpty = true;
for (const idx in process.argv) {
  if (idx >= 2) {
    console.log(process.argv[2]);
    isEmpty = false;
    break;
  }
}

if (isEmpty === true) {
  console.log('No argument');
}
