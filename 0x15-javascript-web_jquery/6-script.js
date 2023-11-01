const divHeader = $('DIV#update_header');
// Select the header element
const headerToChange = $('header');
// Update the text
divHeader.on('click', function () {
  headerToChange.text('New Header!!!');
});
