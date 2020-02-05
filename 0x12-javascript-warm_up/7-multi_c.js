#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(arg, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
}
