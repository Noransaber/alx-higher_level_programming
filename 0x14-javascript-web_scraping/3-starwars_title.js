#!/usr/bin/node
const MovieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieUrl = baseUrl.concat(MovieId);

const request = require('request');

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
