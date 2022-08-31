from .Request import * # Request class imported

# Class in charge of making the request to the API and getting the correct results
class Episode():
  def __init__(self, id):
    self.__request = Request(f"https://rickandmortyapi.com/api/episode/{id}", timeout=2.5).make_episode_request() # Make the request
    
    self.name = [episode["name"] for episode in self.__request] # Get the name of the episode
    self.appearance = self.__request[0]["air_date"] # Get the date of the first episode, the oldest one
