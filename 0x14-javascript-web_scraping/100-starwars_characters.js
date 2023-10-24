#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    let charactersProcessed = 0;
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name;
          characterNames.push(charName);
        }
        charactersProcessed++;
        if (charactersProcessed === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
