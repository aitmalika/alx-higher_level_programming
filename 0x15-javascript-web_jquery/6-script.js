// script that updates this text of the <header> element to New Header!!!
//  when this user clicks on DIV#update_header
const $ = window.$;
$('#update_header').bind('click', function () {
  $('header').replaceWith('New Header!!!');
});
