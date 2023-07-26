#!/usr/bin/node
/* Script that displays the status code of a GET request */
const request = require('request');
request.get(process.argv[2], function (err, res) {
  if (err) { console.log(err); } else { console.log('code: ' + res.statusCode); }
});
