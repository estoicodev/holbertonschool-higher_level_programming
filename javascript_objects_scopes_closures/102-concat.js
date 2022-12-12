#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

const data1 = fs.readFileSync(argv[2], 'utf8');
const data2 = fs.readFileSync(argv[3], 'utf8');
const dataConcat = data1.concat(data2);

fs.writeFileSync(argv[4], dataConcat);
