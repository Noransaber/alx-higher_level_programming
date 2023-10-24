#!/usr/bin/node
const url = process.argv[2];
const fileName = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = body;
  fs.writeFile(fileName, data, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
