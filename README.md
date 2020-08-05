# Casting Agency API

Welcome to my awsome **Casting Agency** API.
This is my capstone project for full stack development nanodegree in udacity.
you can check it live on **Heroku** [here](https://casting-fsnd.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

With Postgres running, run these commands to migrate database:

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server

To run the server, execute:

```bash
python3 app.py
```

## Endpoints request & respose examples

`Note:` All Endpoints require authentication token except the home endpoint (`/`)

### GET '/actors'

- request actors in the database
- Returns:Json opject contains {'succes': True, 'actors': []}
- **sample :** `curl http://127.0.0.1:5000/actors -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
  "actors": [
    {
      "age": 15,
      "gender": "female",
      "id": 1,
      "name": "Nada"
    },
    {
      "age": 15,
      "gender": "female",
      "id": 5,
      "name": "Mayar"
    }
  ],
  "success": true
}
```

### GET '/movies'

- request movies in the database
- Returns:Json opject contains {'succes': True, 'movies': []}
- **sample :** `curl http://127.0.0.1:5000/movies -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "shs movie"
    },
    {
      "id": 4,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "super man"
    },
    {
      "id": 6,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "myshs movie"
    }
  ],
  "success": true
}
```

### DELETE '/actors/<int:id>'

- delete a single actor by id
- Returns: Json opject contains {'succes': True, 'deleted_actor': {}}
- **sample :** `curl -X DELETE http://127.0.0.1:5000/actors -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
 "deleted_actor": {
   "age": 15,
   "gender": "female",
   "id": 1,
   "name": "Hudaasa"
 },
 "success": true
}
```

### DELETE '/movies/<int:id>'

- delete a single movie by id
- Returns: Json opject contains {'succes': True, 'deleted_movie': {}}
- **sample :** `curl -X DELETE http://127.0.0.1:5000/movies -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
 "deleted_movie": {
     "id": 1,
     "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
     "title": "shs movie"
   },
 "success": true
}
```

### POST '/actors'

- create new actor
- Request Arguments: json object contains (name, age, gender)
- Returns: Json opject contains {'succes': True, 'new_actor': {}}
- **sample :** `curl -X POST http://127.0.0.1:5000/actors -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"name":"xox","age":15,"gender":"male"}'`

```
{
  "new_actor": {
    "age": 15,
    "gender": "male",
    "id": 6,
    "name": "xox"
  },
  "success": true
}
```

### POST '/movies'

- create new movie
- Request Arguments: json object contains (title, year, month, day)
- Returns: Json opject contains {'succes': True, 'new_movie': {}}
- **sample :** `curl -X POST http://127.0.0.1:5000/movies -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"title": "End World","year": 2024,"month": 12,"day": 10}'`

```
{
  "new_movie": {
    "id": 7,
    "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
    "title": "End World"
  },
  "success": true
}
```

### PATCH '/actors/<int:id>'

- modify specific actor by id
- Request Arguments: json object contains at least one of these values (name, age, gender)
- Returns: Json opject contains {'succes': True, 'modified_actor': {}}
- **sample :** `curl -X PATHC http://127.0.0.1:5000/actors/6 -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"name":"test"}'`

```
{
  "modified_actor": {
    "age": 15,
    "gender": "male",
    "id": 6,
    "name": "test"
  },
  "success": true
}
```

### PATCH '/movies/<int:id>'

- modify specific movie by id
- Request Arguments: json object contains at least one of these values (title, year, month, day)
- Returns: Json opject contains {'succes': True, 'modified_movie': {}}
- **sample :** `curl -X PATHC http://127.0.0.1:5000/movies/7 -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"year":2026}'`

```
{
  "modified_movie": {
    "id": 7,
    "release_date": "Thu, 10 Dec 2026 00:00:00 GMT",
    "title": "End World"
  },
  "success": true
}
```

## API RBAC

Our API have **3** roles :

### Casting Assistant

- Can view actors and movies

### Casting Director

- All permissions a Casting Assistant has
- Add or delete an actor from the database
- Modify actors or movies

### Executive Producer

- All permissions a Casting Director has
- Add or delete a movie from the database

## Testing

there is a Postman test collection included within the project files
you can use it for testing

you can find fresh tokens in `.env` file
