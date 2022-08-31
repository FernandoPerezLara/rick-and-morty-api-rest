from .Request import *

class Character():
  def __init__(self, name):
    request = Request(f"https://rickandmortyapi.com/api/character/?name={name}")

    characters = request.result

