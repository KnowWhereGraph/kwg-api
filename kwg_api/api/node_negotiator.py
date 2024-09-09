import logging
import os
from typing import Any, Dict

import rdflib
from fastapi import Request, Response
from SPARQLWrapper import JSONLD, QueryResult, SPARQLWrapper
from starlette.responses import FileResponse, RedirectResponse

from kwg_api.lib.content_negotiator import ContentNegotiator
from kwg_api.lib.prefix_builder import PrefixBuilder

logger = logging.getLogger(__name__)

# Mappings from a request mimetype to a rdflib type
RDFLIB_MAPPINGS = {
    "application/n-triples": "n3",
    "application/ld+json": "json-ld",
    "application/rdf+xml": "pretty-xml",
    "text/turtle": "turtle",
}


class NodeNegotiator(ContentNegotiator):
    """
    A content negotiator for nodes. It uses the URI of an object in the graph
    and the 'Accept' header to return information about the node, in a
    particular way (browser redirect or rdf response).
    """

    def __init__(self, request: Request, resource_id: str):
        """
        Initializes a new node negotiator by setting the mappings between
        rdflib and 'Accept' header values.

        :param request: The request object from starlette
        :param resource_id: The identifier of the node
        """
        super().__init__(request, resource_id)

    def negotiate(self) -> Response | RedirectResponse:
        """
        Returns a redirect to an HTML page or returns information about the
        node in a graph format.

        :return: Information about the node or a redirect to a webpage
        """
        if self.request_format not in RDFLIB_MAPPINGS.keys():
            # If nothing was found, direct them to the browser page
            return self._redirect_browse()
        # If the request is for HTML, redirect the request to the browser
        if self.request_format == "text/html":
            # Try to shorten the node URI
            return self._redirect_browse()
        # Otherwise check for RDF serialization formats
        rdf = self._get_rdf()
        return Response(content=rdf, media_type=self.request_format)

    def _get_rdf(self) -> QueryResult.ConvertResult:
        """
        Gets an RDF representation of a node.

        :param node_id: The node's URI
        :return: RDF results with information about the node
        """
        sparql = SPARQLWrapper(f"{self.base_address_https}/sparql")
        query = f"CONSTRUCT {{<{str(self.request_url)}> ?p ?o }} WHERE {{ ?s ?p ?o }}"
        sparql.setQuery(query)
        sparql.setReturnFormat(RDFLIB_MAPPINGS[self.request_format])
        return sparql.queryAndConvert()

    def _redirect_browse(self) -> RedirectResponse:
        """
        Convenience function for sending the requester to the browser.

        :return: A response signaling a redirect to a URL
        """
        browse_url = f"{self.base_browse_address}/browse/"
        resource_id_shortened = PrefixBuilder.resolve_prefix(
            self.request_url, self.resource_id
        )
        if not resource_id_shortened:
            resource_id_shortened = self.resource_id
        print(self.base_address_https)
        return RedirectResponse(url=f"{browse_url}#{resource_id_shortened}")
