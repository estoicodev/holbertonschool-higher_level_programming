#!/usr/bin/node
const axios = require('axios');
axios
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(function (response) {
    const movieTitle = response.data.title;
    console.log(movieTitle);
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });
