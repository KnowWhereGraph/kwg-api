# KWG Content Negotiator
Content negotiation service for KnowWhereGraph


# Running


## Features
The Content Negotiator serves two main user cases:
1. Resolving URIs in a web browser, and expecting to get a new web page describing the resource
2. Robots or others requesting data about a node in an RDF supported format

### Content Negotiation
The current supported RDF mimetypes are
- `application/ld+json`
- `application/n-triples`
- `application/rdf+xml`
- `text/turtle`

## Deploying
To run the API, deploy with docker
1. `docker build -t kwg-api .`
2. `docker run -d --name kwg-deref -p 80:80 kwg-api`

## Logging

## Developing

### Testing




## Troubleshooting

### Connections are refused or 404

### The mimetype isn't being recognised or returns the incorrect format

