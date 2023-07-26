import requests

def get_characters(movie_id):
  url = f"https://swapi.dev/api/films/{movie_id}/characters/"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None

def print_characters(characters):
  for character in characters:
    print(character["name"])

if __name__ == "__main__":
  movie_id = 3
  characters = get_characters(movie_id)
  print_characters(characters)

