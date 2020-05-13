#!/usr/bin/node
const request = require('request');
const request2 = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '?format=json';
request(url, function (error, response) {
  if (error) throw error;
  const info = JSON.parse(response.body);
  for (const i in info.characters) {
    request2(info.characters[i], function (error2, response2) {
      if (error2) throw error2;
      const info2 = JSON.parse(response2.body);
      console.log(info2.name);
    });
  }
});
