from typing import Dict

from starlette.datastructures import Headers
from starlette.requests import Request


def get_parameterized_request(
    headers: Headers | None | Dict[str, str] = None, path: str | None = "/lod/resource/"
) -> Request:
    """
    Creates a 'Request' object representing a mocked client call

    :param headers: A 'Header' object describing the incoming request
    :param path: An optional path. eg /lod/ontology
    :return: A valid 'Request' object
    """
    if headers is None:
        headers = {"Accept": "text/turtle"}
    return Request(
        {
            "type": "http",
            "path": path,
            "headers": Headers(headers).raw,
            "http_version": "1.1",
            "method": "GET",
            "scheme": "https",
            "client": ("127.0.0.1", 8080),
            "server": ("stko-kwg.geog.ucsb.edu", 443),
            "_url": "afakeurl.com",
        }
    )
