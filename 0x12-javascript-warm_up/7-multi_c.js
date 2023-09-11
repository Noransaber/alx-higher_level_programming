#!/usr/bin/node

const num = parseInt(process.argv[2]);
let i;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
