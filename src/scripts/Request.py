import requests

# Class in charge of making the request to the API
class Request():
  def __init__(self, request, timeout=2.5):
    self.__request = request
    self.__timeout = timeout
  
  # Function in charge of searching a character by name
  def make_character_request(self):
    request = requests.get(f"{self.__request}", timeout=self.__timeout) # Make the request

    # Checks if the request was successful
    if request.status_code == 200:
      response = request.json() # Convert the response to JSON

      pages = response["info"]["pages"] # Get the number of pages

      # This condition prevents a quest with a single character from having multiple requests
      if pages > 1:
        # Loop through all the pages
        for page in range(2, pages + 1):
          response["results"].extend(requests.get(f"{self.__request}&page={page}", timeout=self.__timeout).json()["results"]) # Add the results to the response

      return response["results"] # Return the response
    else:
      return []

  # Function in charge of searching an episode by ID
  def make_episode_request(self):
    request = requests.get(f"{self.__request}", timeout=self.__timeout) # Make the request

    # Checks if the request was successful
    if request.status_code == 200:
      return request.json() # Return the response
    else:
      return []
