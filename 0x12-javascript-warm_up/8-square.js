#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  const num = Number(arg);
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
