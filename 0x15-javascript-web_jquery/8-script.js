$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (let i of data['results']) {
    $('#list_movies').append('<li>' + i.title + '</li>');
  }
});
