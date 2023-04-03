# Casting Agency Capstone Project

This is the final project of Full Stack Nanodegree covering all the aspects covered in the course in one project. The project contains two get methods for both getAll movies and actors, getByid for both, update and delete for both of them as well


It migrates and seeds the database with one movie and one actor, whenever the server is run:

* Creates a movie entry into the database
* Creates a actor entry into the database

It has one to many relatinship, (A movie can have multiple actors). Please patch actors to assign them a movie

## How to run this project
* Run `pip install` for installing dependencies from requirements.txt
* Run `FLASK_APP=app.py flask run`
* Create database with the named casting_agency. That's it. No need to add any table or data.
* Also please create a .env file with the following content (you can change db settings as per your requirements)

## Environment variables
DB_USER=postgres
DB_PASSWORD=12345
DB_HOST=localhost:5433
DB_NAME=casting_agency

AUTH0_DOMAIN=dev-c67acshinun1vt55.us.auth0.com
API_AUDIENCE=capstone-api-iden

## Running the test
Please run `python app.py` to run the tests, it connects with the same database. It tests for crud operations. You can change the bearer token in the test file.
## Auth0 url to get token:
https://dev-c67acshinun1vt55.us.auth0.com/authorize?audience=capstone-api-iden&response_type=token&client_id=hJCLrfJaGBCBILnUMAlgt7rwsZCewkRO&redirect_uri=http://127.0.0.1:5000/login_result

## In order to get token, Executive Producer credentials:
Email: executive123@producer456.com

Pass: executive123@producer456.com

## Live deployed site on Render
### The app is deployed: https://casting-agency-uavk.onrender.com/
Please wait few minutse for site to load first time to wake up from sleep

# API Documentation
You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

## Base URL
Local: http://127.0.0.1:5000/
Live: https://casting-agency-uavk.onrender.com/

`GET '/movies'`

- Fetches a list of movies as well as the array of actors.
- Request Arguments: Null
- Returns: A list of items having title and date

Sample response:
```json
{
    "resp": [
        {
            "actors": [
                {
                    "age": 30,
                    "gender": "Female",
                    "id": 1,
                    "name": "Mahira Khan"
                }
            ],
            "date": "1972-03-24",
            "id": 1,
            "title": "Maula Jutt"
        }
    ],
    "status": "OK"
}

```
`GET '/actors'`

- Fetches a list of actors
- Request Arguments: Null
- Returns: A list of actors having name,age,gender and movie name (if they are assigned)

Sample response:
```json
{
    "resp": [
        {
            "age": 30,
            "gender": "Female",
            "id": 1,
            "movie": "Maula Jutt",
            "name": "Mahira Khan"
        }
    ],
    "status": "OK"
}

```

`GET '/movies/id'`

- Fetches a pariclar movie by id
- Request Arguments: id
- Returns: A movie having title and age, and actors if any

Sample response:
```json
{
    "resp": [
        {
            "actors": [
                {
                    "age": 30,
                    "gender": "Female",
                    "id": 1,
                    "name": "Mahira Khan"
                }
            ],
            "date": "1972-03-24",
            "id": 1,
            "title": "Maula Jutt"
        }
    ],
    "status": "OK"
}
```

`GET '/actors/id'`

- Fetches a pariclar actor by id
- Request Arguments: id
- Returns: An actor having name, age,gender, movie if any

Sample response:
```json
{
    "resp": [
        {
            "age": 30,
            "gender": "Female",
            "id": 1,
            "movie": "Maula Jutt",
            "name": "Mahira Khan"
        }
    ],
    "status": "OK"
}
```


`POST '/movies'`

- Fetches a pariclar movie by id
- Request Arguments: body with title, date
- Returns: id of created

Sample response:
```json
{
    "resp": 2,
    "status": "OK"
}
```


`POST '/actors'`

- Fetches a pariclar actor by id
- Request Arguments: body with name, age, gender
- Returns: id of created

Sample response:
```json
{
    "resp": 2,
    "status": "OK"
}
```



`PATCH '/movies'`

- Update a pariclar movie by id
- Request Arguments: body with title and date
- Returns: id of created

Sample response:
```json
{
    "resp": 2,
    "status": "OK"
}
```


`PATCH '/actors'`

- Update a pariclar actor by id
- Request Arguments: body with age,name, gender and movie_id. Also it will be used to assign a movei to actor
- Returns: id of created

Sample response:
```json
{
    "resp": 2,
    "status": "OK"
}
```

`DELETE '/movies/id'`

- Delete a pariclar movie by id
- Request Arguments: id
- Returns: id of created

Sample response:
```json
{
    "resp": 1,
    "status": "OK"
}
```

`DELETE '/actors/id'`

- Delete a pariclar actor by id
- Request Arguments: id
- Returns: id of created

Sample response:
```json
{
    "resp": 1,
    "status": "OK"
}
```