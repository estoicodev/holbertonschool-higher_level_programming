#!/usr/bin/node
const axios = require('axios');
axios
  .get(process.argv[2])
  .then(function (response) {
    console.log(`code: ${response.status}`);
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });
