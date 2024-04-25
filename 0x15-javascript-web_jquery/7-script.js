// script that fetches this character name from the URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').append(data.name);
});
