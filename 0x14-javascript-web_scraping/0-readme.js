#!/usr/bin/node
const fs = require('fs');

function readData (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
}

fs.readFile(process.argv[2], 'utf8', readData);
