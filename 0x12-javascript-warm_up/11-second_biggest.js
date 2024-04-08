#!/usr/bin/node

/*
 * Subtract 2 to account for node and file
 */

const argv = process.argv.length - 2;

if (argv === 0) {
  console.log('0');
} else if (argv === 1) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
