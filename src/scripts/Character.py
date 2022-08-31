from .Request import *

class Character():
  def __init__(self, name):
    request = Request(f"https://rickandmortyapi.com/api/character/?name={name}").result
    self.characters = [self.__create_character(character) for character in request]

  def __create_character(self, character):
    new_character = {
      "name": character["name"]
    }

    return new_character
