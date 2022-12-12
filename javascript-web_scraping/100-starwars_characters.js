#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, res, body) {
      if (err) {
        console.error('error:', err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
