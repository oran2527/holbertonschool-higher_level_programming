#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + '?format=json';
let count = 0;
request(url, function (error, response, body) {
  if (error) throw error;
  const info = JSON.parse(response.body);
  for (let i = 0; i < info.count; i++) {
    for (let j = 0; j < info.results[i].characters.length; j++) {
      if (info.results[i].characters[j].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
