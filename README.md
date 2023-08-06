# KWG API
API service for KnowWhereGraph


## Running
To run the API, deploy with docker
1. `docker build -t kwg-api .`
2. `docker run -d --name kwg-api -p 80:80 kwg-api`


 http://127.0.0.1:8000/redoc

Visit the swagger page at 

## Features

- Node de-referencing
- Common vocabulary retrieval


## Logging

## Developing

Changes should be submitted as a pull request to the `development` branch.

A number of tools should be run before submitting the pull request.

```bash
poetry run mypy .
poetry run black .
poetry run isort .
```

### Testing

The unit tests can be run through pytest with

`poetry run pytest`

#### Coverage

To generate coverage stats, run

`poetry run`


## Building Docs
The API uses the sphinx documentation formation. To build the docuementation