#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '?format=json';
request(url, function (error, response) {
  if (error) throw error;
  const info = JSON.parse(response.body);
  console.log(info.title);
});
