#!/usr/bin/node
const request = require('request');
const axios = require('axios');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (err, res, body) {
  if (err) {
    console.error('error:', err);
  }
  const characters = JSON.parse(body).characters;
  const endpoints = [...characters];
  axios
    .all(endpoints.map(endpoint => axios.get(endpoint)))
    .then(function (response) {
      const responseKeys = Object.keys(response);
      for (let i = 0; i < responseKeys.length; i++) {
        console.log(response[i].data.name);
      }
    });
});

// request(url, async function (err, res, body) {
//   if (err) {
//     console.error('error:', err);
//   }
//   const characters = JSON.parse(body).characters;
//   for (let i = 0; i < characters.length; i++) {
//     request(characters[i], async function (err, res, body) {
//         if (err) {
//           console.error('error:', err);
//         }
//         console.log(JSON.parse(body).name);
//     })
//   }
// });
