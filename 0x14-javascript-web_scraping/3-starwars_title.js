#!/usr/bin/node
const request = require('request');
const end = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + end, function (error, respones, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
