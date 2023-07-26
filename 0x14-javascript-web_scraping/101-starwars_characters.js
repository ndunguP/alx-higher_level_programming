import axios from "axios";
// Define the base URL for the Star Wars API.
const BASE_URL = "https://swapi.dev/api/";
// Define the endpoint for getting the list of characters in a movie.
const CHARACTERS_ENDPOINT = "films/{movie_id}/characters";
// Get the movie ID from the user.
const movie_id = prompt("Enter the movie ID:");
// Make the request to the API.
axios
  .get(BASE_URL + CHARACTERS_ENDPOINT, {
    params: { movie_id },
  })
  .then((response) => {
    // Get the response from the API.
    const characters = response.data.results;
    // Print each character name on a separate line.
    characters.forEach((character) => console.log(character.name));
  })
  .catch((error) => console.error(error));
