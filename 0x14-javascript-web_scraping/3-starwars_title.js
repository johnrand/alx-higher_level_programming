#!/usr/bin/node

/**
 * script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */

const request = require('request');
const episodeNo = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNo, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
