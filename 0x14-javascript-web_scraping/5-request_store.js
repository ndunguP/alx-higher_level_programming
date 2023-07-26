#!/usr/bin/node
/* Script that gets the contents of a webpage
and stores it in a file */
const request = require('request');
const fs = require('fs');
let url = process.argv[2];
request(url, 'utf8', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
