#!/usr/bin/node

const x = parseInt(process.argv[2]);
let i, j;

if (!x || typeof (x) !== 'number') {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    let line = '';
    for (j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
