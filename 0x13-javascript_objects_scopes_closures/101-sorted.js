#!/usr/bin/node

/**
 * script that imports a dictionary of occurrence by user id and
 * compute a dictionary of user ids by occurrence.
 * Your script must import dict from this file 101-data.js.
 * In this new dictionary: A key is a number of occurrences, a value is
 * this list of user ids.
 * Print this new dictionary at the end
 */
const initDict = require('./101-data').dict;
const newDict = {};

for (const key in initDict) {
  if (newDict[initDict[key]] === undefined) {
    newDict[initDict[key]] = [];
  }
  newDict[initDict[key]].push(key);
}
console.log(newDict);
