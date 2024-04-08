#!/usr/bin/node

/*
 * Subtract 2 to account for node and file
 */

const argv = process.argv.length - 2;

if (argv === 0) {
  console.log('No argument');
} else if (argv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
