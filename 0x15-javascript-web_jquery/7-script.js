// Get the url
const characterUri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
// Get the character dev
const $characterDiv = $('div#character');

// AJAX syntax to display the name
$.ajax({
  url: characterUri,
  dataType: 'json'
}).done((data) => {
  $characterDiv.text(data.name);
});
