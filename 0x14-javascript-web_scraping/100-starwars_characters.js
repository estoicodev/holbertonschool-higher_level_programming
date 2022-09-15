#!/usr/bin/node
const axios = require('axios');
axios
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(function (response) {
    const movie = response.data;
    const endpoints = [...movie.characters];
    axios
      .all(endpoints.map(endpoint => axios.get(endpoint)))
      .then(function (response) {
        const responseKeys = Object.keys(response);
        for (let i = 0; i < responseKeys.length; i++) {
          console.log(response[i].data.name);
        }
      });
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });
