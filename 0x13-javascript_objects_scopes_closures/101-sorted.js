#!/usr/bin/node

const dict = require('./101-data').dict;
let listValues = [];
let listKeys = [];
let uniqueIds = [];
let sortKeys = [];
const finalDict = {};

for (const key in dict) {
  listValues.push(dict[key]);
}
uniqueIds = Array.from(new Set(listValues));
for (let i = 0; i < uniqueIds.length; i++) {
  for (const key in dict) {
    if (uniqueIds[i] === dict[key]) {
      listKeys.push(key);
    }
  }
  sortKeys = listKeys.sort();
  finalDict[uniqueIds[i]] = sortKeys;
  listKeys = [];
  sortKeys = [];
}
listValues = [];
listKeys = [];
console.log(finalDict);
