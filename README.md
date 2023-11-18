# KWG API

API service for KnowWhereGraph

## Running

The API service is meant to be run under full stack operating conditions. There are several flavors of the API, which correspond to different docker-compose files.

1. local: Uses a local GraphDB deployment
2. stage: Uses the staging GraphDB deployment
3. prod: Uses the production GraphDB deployment

### Outside of the Stack

To run the API in a production setting, outside the full stack, deploy with docker using

```bash
docker-compose -f docker-compose.dev.yaml up
```

This avoids the inclusion of the service in the `kwg_netowrk`, which is used when doing a full stack deployment.

Visit the redoc page at http://localhost/redoc

Visit the swagger page at http://localhost/docs

Test the redirection with http://localhost/lod/resource/hazard.1183609.5434007


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
