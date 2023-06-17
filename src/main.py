import json
import logging
import os

from fastapi import FastAPI, Request, Response
from starlette.responses import RedirectResponse
from SPARQLWrapper import SPARQLWrapper, JSONLD


from src.api.content_negotiator import ContentNegotiator
from src.api.v1.vocabulary_builder import VocabularyBuilder

app = FastAPI(
    title="",
    version="1.0.0"
)
logging.basicConfig(level=logging.INFO)


@app.get(
    "/lod/resource/{resource_id}",
    summary="Resolve the resource",
    description="Resolves a resource based on the type specified in the 'Accept' header."
)
async def lod(request: Request, resource_id: str):
    logging.info(f"Processing lod request for {resource_id}")
    content_negotiator = ContentNegotiator(request, resource_id)
    return content_negotiator.negotiate()
