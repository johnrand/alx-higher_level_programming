#!/usr/bin/node

/**
 * script that prints the number of movies where the
 * character “Wedge Antilles” is present with ID 18.
 */

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body).result;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
