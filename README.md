<br />
<p align="center">
  <a href="https://github.com/FernandoPerezLara/rick-and-morty-api-rest">
    <img src="https://assets.stickpng.com/thumbs/58f37720a4fa116215a9240f.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Rick & Morty: REST API</h3>

  <p align="center">
    Rest API to search Rick and Morty characters
    <br />
    <a href="https://rickandmortyapi.com/"><strong>Visit website »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FernandoPerezLara/rick-and-morty-api-rest/tree/main">View Code</a>
    ·
    <a href="https://github.com/FernandoPerezLara/rick-and-morty-api-rest/issues">Report Bug</a>
  </p>
</p>
<br />

The aim of this project is to create a rest API in charge of querying and searching for Rick and Morty characters from a given database.

## How does it work?
When you make a request, searching for the name of a character, you get a list of all the results found.

The problem is that these are divided into pages of 20 characters, so you have to go through all the pages to get all the desired results. For this, a function has been created in the `Character` class in charge of doing this job, avoiding executing more than once the requests that do not have more than one page.

Once the characters are obtained, the episodes where they appear are taken, obtaining the ID and making another request to the database to obtain their names.

To show the episode where each character appears, the first one has been selected, since it will always be the predecessor of all the others.

## Installation and execution
In order to facilitate the deployment of this project, the installation and execution of the program is done with Docker.

First, it will be necessary to download the repository and access it from the terminal:
```
git clone https://github.com/FernandoPerezLara/rick-and-morty-api-rest.git
cd rick-and-morty-api-rest
```

Once you have the repository downloaded, executing the following command will display a container with the program:
```
docker-compose up
```

> NOTE: If you want to remove the container, you can do it with the command `docker-compose down`.

To test that the program works correctly, it can be checked by accessing to `https://rickandmortyapi.com/api/character/?name=rick%20sanchez`.

## Project structure
The project code can be found inside the `./src/` folder.

The file `main.py` will be in charge of creating the server capable of receiving the requests made by the user. It uses the functions developed to obtain the characters and episodes, found in the `./src/scripts/` folder.
```
src
├── scripts
│   ├── Character.py
│   ├── Episode.py
│   └── Request.py
├── main.py
└── ···
```

## Contributors
- [Fernando Pérez Lara](https://www.linkedin.com/in/fernandoperezlara/) ([**@FernandoPerezLara**](https://github.com/FernandoPerezLara)) for developing this project.
