import logging
import os

from fastapi import Request, Response
from SPARQLWrapper import JSONLD, SPARQLWrapper
from starlette.responses import FileResponse, RedirectResponse

from kwg_api.lib.prefix_builder import PrefixBuilder


class OntologyNegotiator:
    """
    The OntologyNegotiator is responsible for serving ontology data
    """

    def __init__(self, request: Request) -> None:
        """

        :param request:
        """

    def negotiate(self):
        """
        Decides whether to return HTML or some other format
        :return:
        """
