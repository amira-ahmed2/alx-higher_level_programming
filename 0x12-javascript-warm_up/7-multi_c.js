#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = number 
if (!isNaN(i)) {
while (i) {
	console.log("C is fun");
	i --;
}
} else {
	  console.log("Missing number of occurrences");
}
