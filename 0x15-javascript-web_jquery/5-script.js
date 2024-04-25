// script that adds a <li> element to a list when this user clicks on this
// tag DIV#add_item
const $ = window.$;
$('#add_item').bind('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
