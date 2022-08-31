from flask import Flask, request

from scripts import * # Created classes are imported

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True # Pretty print JSON

# Function in charge of showing a message when the client is on "/"
@app.route("/")
def main():
  return "To search, you must make a request like the following example: \"http://127.0.0.1:5000/search-character-appearance?name=Rick%20Sanchez\"."

# Function in charge of searching a character by name and showing the result
@app.route("/search-character-appearance")
def search_character():
  name = request.args.get("name") # Get the name from the request

  characters = Character(name=name).characters # Search the character by name

  if len(characters) != 0:
    return characters # Show the result

  return "No results found." # Show a message if no results were found

# Function in charge of displaying a message if there is an error
@app.errorhandler(404)
def not_found(error):
  return f"404, Page not found"

if __name__ == "__main__":
  main()
