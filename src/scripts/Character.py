from .Request import *
from .Episode import *

class Character():
  def __init__(self, name):
    request = Request(f"https://rickandmortyapi.com/api/character/?name={name}").make_character_request()
    self.characters = [self.__create_character(character) for character in request]

  def __create_character(self, character):
    episodes_id = [int(episode.split("/")[-1]) for episode in character["episode"]]
    episodes = Episode(episodes_id)

    new_character = {
      "name": character["name"],
      "episode": episodes.name,
      "appearance": episodes.appearance
    }

    return new_character
