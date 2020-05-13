#!/usr/bin/node
const request = require('request');
const request2 = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '?format=json';
request(url, function (error, response) {  
  if (error) throw error;
  const info = JSON.parse(response.body);
  for (const i in info.characters) {
    let list_chars[list_chars.length] = info.characters[i];
  }  
});
request.end;
console.log(list_chars);
for (j in list_chars) {
  request2(j, function (error2, response2) {
    if (error2) throw error2;
    const info2 = JSON.parse(response2.body);            
    let list_chars_2[list_chars_2.length] = info2.name;              
  });
}  


