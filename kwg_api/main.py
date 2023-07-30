import json
import logging

import uvicorn
from fastapi import FastAPI, Request, Response

from kwg_api.api.node_negotiator import NodeNegotiator
from kwg_api.lib.prefix_builder import PrefixBuilder

app = FastAPI(title="KnowWhereGraph API", version="1.0.0")
logging.basicConfig(level=logging.INFO)


@app.get(
    "/lod/ontology/{resource_id}",
    summary="Get information about an ontology term",
    description="The KnowWhereGraph ontology is loaded into the backing graph database. During the process of mapping"
    "an ontology term to a node, a unique identifier is assigned to the node. This endpoint takes the"
    "URI of a node representing an ontology term and returns information about it.",
    tags=["Node Information"],
)
async def get_resource(request: Request, resource_id: str) -> Response | None:
    """
    Gets information about a node by
    1. Redirecting to a URL with information on it
    2. Returning an RDF format, if specified by the 'Accept' header

    :param request: The request details
    :param resource_id: The node id (eg stko-kwg.geog.ucsb/edu/lod/resource/resource_id
    :return: A response that either redirects or has RDF
    """
    return NodeNegotiator(request, resource_id).negotiate()


@app.get(
    "/lod/resource/{resource_id}",
    summary="Get information about a KnowWhereGraph resource",
    description="Retrieves information about a resource type node in the graph database..",
    tags=["Node Information"],
)
async def get_ontology_resource(request: Request, resource_id: str) -> Response | None:
    """
    Gets information about a node describing an aspect of an onotology by
    1. Redirecting to a URL with information on it
    2. Returning an RDF format, if specified by the 'Accept' header

    :param request: The request details
    :param resource_id: The node id (eg stko-kwg.geog.ucsb/edu/lod/ontology/resource_id
    :return: A response that either redirects or has RDF
    """
    return NodeNegotiator(request, resource_id).negotiate()


@app.get(
    "/vocabulary",
    summary="Fetch KnowWhereGraph's prefix",
    description="Returns a mapping of URI -> prefix for all vocabularies used by KnowWhereGraph",
    tags=["Semantic Integration"],
)
async def get_vocabulary(request: Request) -> Response:
    """
    Builds and returns the set of vocabulary terms that KWG uses

    :param request:
    :return:
    """
    return Response(json.dumps(PrefixBuilder().build(), indent=2))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
