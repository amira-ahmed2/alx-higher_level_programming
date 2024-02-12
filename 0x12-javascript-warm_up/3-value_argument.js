#!/usr/bin/node

const argsCount = process.argv[2];
if (!argsCount) {
  console.log('No argument');
} else {
  console.log(argsCount);
}
