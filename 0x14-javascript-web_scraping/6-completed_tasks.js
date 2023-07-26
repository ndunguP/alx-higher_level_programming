#!/usr/bin/node
/* Script that computes the number of tasks completed by user id */
const request = require('request');
let url = process.argv[2];
request(url, 'utf8', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    let result = JSON.parse(body);
    for (let key = 0; key < result.length; key++) {
      if (result[key].completed === true) {
        if (result[key].userId in dict) {
          dict[result[key].userId]++;
        } else {
          dict[result[key].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
