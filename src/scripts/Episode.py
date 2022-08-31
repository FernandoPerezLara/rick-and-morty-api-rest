import time

from .Request import *

class Episode():
  def __init__(self, id):
    self.__request = Request(f"https://rickandmortyapi.com/api/episode/{id}").make_episode_request()
    
    self.name = [episode["name"] for episode in self.__request]
    self.appearance = self.__request[0]["air_date"]
