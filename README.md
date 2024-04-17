# KWG API

API service for KnowWhereGraph

## Features

- Node de-referencing
- Common vocabulary retrieval

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

```commandline
poetry run pytest
```


## Building Docs

The API uses the sphinx documentation formation. To build the documentation, first [install sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html).

Then,

```commandline
cd docs
make build
```

## Running

When the API is running, the following pages can be used to play with the endpoint

Visit the redoc page at http://127.0.0.1:8080/redoc

Visit the swagger page at http://127.0.0.1:8080/docs


The API can be run locally when developing. To run,

### For local Development

#### Non-Docker

```bash
poetry install
poetry run uvicorn kwg_api.main:app --reload --port 80
```

### With Docker

The API can also be run using the `docker-compose.dev.yaml` file with

```commandline
docker-compose -f docker-compose.dev.yaml up
```
