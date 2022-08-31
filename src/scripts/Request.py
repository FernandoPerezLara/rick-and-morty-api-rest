import requests

class Request():
  def __init__(self, request):
    self.__request = request
    
  def make_character_request(self):
    request = requests.get(f"{self.__request}").json()
    pages = request["info"]["pages"]

    if pages > 1:
      for page in range(2, pages + 1):
        request["results"].extend(requests.get(f"{self.__request}&page={page}").json()["results"])

    return request["results"]

  def make_episode_request(self):
    return requests.get(f"{self.__request}").json()
