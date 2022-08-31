from flask import Flask, request

from scripts import *

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route("/")
def main():
  return "To search, you must make a request like the following example: \"http://127.0.0.1:5000/search-character-appearance?name=Rick%20Sanchez\"."

@app.route("/search-character-appearance")
def search_character():
  name = request.args.get("name")

  characters = Character(name=name).characters

  if len(characters) != 0:
    return characters

  return "No results found."

@app.errorhandler(404)
def not_found(error):
  return f"404, Page not found"

if __name__ == "__main__":
  main()
