#!/usr/bin/node
const request = require('request');

// const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.error('error:', err);
  }
  const movies = JSON.parse(body).results;
  let countCharacter18InMovies = 0;
  for (let i = 0; i < movies.length; i++) {
    const characters = movies[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const urlTokens = characters[j].split('/');
      const idCharacter = Number(urlTokens[urlTokens.length - 2]);
      if (idCharacter === 18) {
        countCharacter18InMovies += 1;
        break;
      }
    }
  }
  console.log(countCharacter18InMovies);
});
