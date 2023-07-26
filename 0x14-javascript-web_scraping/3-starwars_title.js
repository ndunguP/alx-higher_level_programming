#!/usr/bin/node
/* Script that prints the title of a Star Wars movie
where the episode number matched a given integer */
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2] + '/';
request.get(url, function (err, res, body) {
  if (err) { console.log(err); } else { console.log(JSON.parse(body).title); }
});
