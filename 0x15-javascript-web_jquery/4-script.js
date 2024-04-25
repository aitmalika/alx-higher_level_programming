// script that toggles this class of the <header> element when the user
// clicks on this tag DIV#toggle_header
const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});
