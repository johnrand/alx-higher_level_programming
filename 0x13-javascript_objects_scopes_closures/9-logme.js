#!/usr/bin/node

/*
 * function that prints the number of arguments
 * already printed and the new argument value
 */

let numberArg = 0;

exports.logMe = function (item) {
  console.log(numberArg + ': ' + item);
  numberArg++;
};
