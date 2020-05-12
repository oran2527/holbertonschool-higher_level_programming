#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + '?format=json';
const dict = {};
let val = 1;
request(url, function (error, response) {
  if (error) throw error;
  const info = JSON.parse(response.body);
  for (let i = 0; i < info.length; i++) {
    val = 1;
    if (info[i].completed === true) {
      if (dict[info[i].userId]) {
        val = dict[info[i].userId] + 1;
      }
      dict[info[i].userId] = val;
    }
  }
  console.log(dict);
});
