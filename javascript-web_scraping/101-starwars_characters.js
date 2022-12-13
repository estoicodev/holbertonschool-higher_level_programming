#!/usr/bin/node
const request = require('request');

const URL_BASE = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(URL_BASE, function (err, res, body) {
  if (err) {
    console.error('error:', err);
    return;
  }
  const characters = JSON.parse(body).characters;
  const promises = characters.map(function (characterUrl) {
    return new Promise(function (resolve, reject) {
      request(characterUrl, function (err, res, body) {
        if (err) {
          console.error('error:', err);
          return;
        }
        const name = JSON.parse(body).name;
        if (name) {
          resolve(name);
        } else {
          reject(err);
        }
      });
    });
  });
  Promise.all(promises)
    .then(function (names) {
      names.forEach(function (n) {
        console.log(n);
      });
    });
});
