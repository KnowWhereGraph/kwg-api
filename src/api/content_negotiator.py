import logging
import os

from fastapi import Request, Response
from starlette.responses import RedirectResponse
from SPARQLWrapper import SPARQLWrapper, JSONLD

from src.api.vocabulary_builder import VocabularyBuilder


class ContentNegotiator:

    def __init__(self, request: Request, resource_id: str):
        """
        Creates a new ContentNegotiator
        """
        self.base_address = os.getenv('base_address')
        self.request_format = request.headers.get('accept')
        self.resource_id = resource_id
        self.node_id = request.url._url
        self.rdflib_mappings = {
            'application/n-triples': 'n3',
            'application/ld+json': 'json-ld',
            'application/rdf+xml': 'pretty-xml',
            'text/turtle': 'turtle'
        }

    def negotiate(self):
        """
        Returns a redirect to an HTML page or returns information about the
        node in a graph format.
        :return: Information about the node
        """
        browse_url = f'{self.base_address}/browse/'
        # If the request is for HTML, redirect the request to the browser
        if self.request_format == 'text/html':
            response = RedirectResponse(url=f'{browse_url}#{self.resolve_prefix()}')
            return response
        # Otherwise check for RDF serialization formats
        try:
            rdf = self._get_rdf().serialize(format=self.rdflib_mappings[self.request_format])
            return Response(content=rdf, media_type=self.request_format)
        except KeyError:
            # If KeyError is thrown, there wasn't a match for rdflib serializations
            pass
        # If nothing was found, direct them to the browser
        return RedirectResponse(url=f'{browse_url}#{self.resolve_prefix()}')

    def _get_rdf(self):
        """
        Gets an RDF representation of the node
        :return: RDF result with information about the node
        """
        sparql = SPARQLWrapper(f"{self.base_address}/sparql")
        query = f"CONSTRUCT {{<{self.node_id}> ?p ?o }} WHERE {{ ?s ?p ?o }}"
        sparql.setQuery(query)
        sparql.setReturnFormat(JSONLD)
        return sparql.queryAndConvert()

    def resolve_prefix(self) -> str:
        """
        Given a full node URI, replace as much as the URI as possible with a prefix.
        :return: The URI, prefixed
        """
        res = f"{self.base_address}/lod/resource/"
        ont = f"{self.base_address}/lod/ontology/"
        print(res)
        print(ont)
        # Get the supported prefixes
        vocab = VocabularyBuilder().build()
        for key, val in vocab.items():
            print(val)
        try:
            logging.info(f"Resolving prefix for {self.base_address}")
            prefix = next(key for key, value in vocab.items() if (value == res or value == ont))
            return f"{prefix}:{self.resource_id}"
        except StopIteration:
            return self.node_id
