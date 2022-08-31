import requests

class Request():
  def __init__(self, request):
    self.__request = request
    
  def make_character_request(self):
    request = requests.get(f"{self.__request}")

    if request.status_code == 200:
      response = request.json()

      pages = response["info"]["pages"]

      if pages > 1:
        for page in range(2, pages + 1):
          response["results"].extend(requests.get(f"{self.__request}&page={page}").json()["results"])

      return response["results"]
    else:
      return []

  def make_episode_request(self):
    request = requests.get(f"{self.__request}")

    if request.status_code == 200:
      return request.json()
    else:
      return []
