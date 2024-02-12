#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const number = parseInt(process.argv[2]);
  let i = 0;
  while (i < number) {
    console.log('X'.repeat(number));
    i++;
  }
}
