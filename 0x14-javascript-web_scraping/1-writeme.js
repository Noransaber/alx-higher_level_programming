#!/usr/bin/node

const file = process.argv[2];
const stringToWrite = process.argv[3];

const fs = require('fs');

fs.writeFile(file, stringToWrite, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  }
});
