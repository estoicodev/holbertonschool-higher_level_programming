#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
axios
  .get(process.argv[2])
  .then(function (response) {
    const data = response.data;
    fs.writeFile(
      process.argv[3],
      data,
      { encoding: 'utf8' },
      function (err, data) {
        if (err) {
          console.log(err);
        }
      }
    );
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });
