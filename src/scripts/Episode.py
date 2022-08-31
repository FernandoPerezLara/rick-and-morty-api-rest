import time

from .Request import *

class Episode():
  def __init__(self, id):
    request = Request(f"https://rickandmortyapi.com/api/episode/{id}").make_episode_request()
    self.name = [episode["name"] for episode in request]
    self.appearance = request[0]["air_date"]
