#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const path = process.argv[3];
const url = process.argv[2];
request(url, function (error, response) {
  if (error) throw error;
  const text = response.body;
  fs.writeFile(path, text, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
