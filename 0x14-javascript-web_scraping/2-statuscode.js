#!/usr/bin/node

const URL = process.argv[2];

const request = require('request');

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
