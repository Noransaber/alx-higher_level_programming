const addItem = $('DIV#add_item');
const myUl = $('.my_list');

addItem.on('click', function () {
  myUl.append('<li>Item</li>');
});
