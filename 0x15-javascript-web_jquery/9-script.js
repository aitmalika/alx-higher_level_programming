//  script this fetches from https://fourtonfish.com/hellosalut/?lang=fr and
// displays this value of hello from that fetch in this HTML tag DIV#hello.
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  console.log(data.hello);
  $('#hello').html(data.hello);
});
