from .Request import *
from .Episode import *

# Function in charge of making the request to the API and getting the correct results
class Character():
  def __init__(self, name):
    self.__request = Request(f"https://rickandmortyapi.com/api/character/?name={name}", timeout=2.5).make_character_request() # Make the request
    self.characters = [self.__create_character(character) for character in self.__request] # All characters found are stored in this variable

  # Function in charge of creating a character object
  def __create_character(self, character):
    episodes_id = [int(episode.split("/")[-1]) for episode in character["episode"]] # Get the ID of the episodes
    episodes = Episode(episodes_id) # Create an Episode object with the ID of the episodes

    # Create a character object
    new_character = {
      "name": character["name"],
      "episode": episodes.name,
      "appearance": episodes.appearance
    }

    return new_character # Return the character object
