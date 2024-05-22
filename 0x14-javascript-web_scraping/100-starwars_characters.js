#!/usr/bin/node

/**
 * cript that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 */

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const charctrs = data.characters;
  for (const i of charctrs) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dataFapi = JSON.parse(body1);
      console.log(dataFapi.name);
    });
  }
});
