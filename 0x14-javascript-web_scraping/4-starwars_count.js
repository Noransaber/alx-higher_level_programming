#!/usr/bin/node
const url = process.argv[2];
const id = 18;

const fullUrl = url.concat(id);
const request = require('request');

request(fullUrl, (err, res, body) => {
if (err) {
	console.error(err);
}
const data = JSON.parse(body).films;
const len = data.length;
console.log(len);
});
