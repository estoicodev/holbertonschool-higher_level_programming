#!/usr/bin/node
const axios = require('axios');
axios
  .get(process.argv[2])
  .then(function (response) {
    const movies = response.data.results;
    let countCharacterId18 = 0;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const arrayOfStrings = characters[j].split('/');
        const characterId = arrayOfStrings[arrayOfStrings.length - 2];
        if (characterId === '18') {
          countCharacterId18++;
        }
      }
    }
    console.log(countCharacterId18);
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });
