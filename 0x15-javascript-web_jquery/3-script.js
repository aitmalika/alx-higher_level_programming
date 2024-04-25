// script that adds the class red to this <header> element when the user
// clicks on this tag DIV#red_header
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').addClass('red');
});
