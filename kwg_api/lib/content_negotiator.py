import logging
import os

from fastapi import Request, Response

logger = logging.getLogger(__name__)


class ContentNegotiator:
    """
    Base class for content negotiators. It initializes the class with
    several convenient variables and member functions
    """

    def __init__(self, request: Request, resource_id: str):
        """
        Creates a new ContentNegotiator.
        """
        self.base_address_http = os.getenv("base_address_http")
        self.base_address_https = os.getenv("base_address_https")
        accept_header = request.headers.get("accept")
        if not accept_header:
            raise ValueError("Failed to read the request headers")
        self.request_format = accept_header.lower()
        self.request_url = request.url
        self.resource_id = resource_id

    def negotiate(self):
        """
        Negotiates a request. This method should be implemented by subclasses

        :return: A response to the request
        """
        logger.error(
            "The 'negotiate' method of the ContentNegotiator base class was called, which"
            "is not intended."
        )
        raise NotImplementedError("Base class does not support negotiation")
