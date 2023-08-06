import os
import unittest.mock
from typing import Callable
from unittest.mock import patch

import pytest
from starlette.datastructures import Headers
from starlette.requests import Request
from starlette.responses import RedirectResponse

import kwg_api.api.node_negotiator
from kwg_api.api.node_negotiator import NodeNegotiator
from tests.utils.shared_methods import get_parameterized_request


def test_init() -> None:
    """
    Tests that we can construct negotiators

    :return: None
    """
    assert NodeNegotiator(get_parameterized_request(), "kwgr:zipCodeArea.99924")


def test_no_content_found() -> None:
    """
    Tests that when a matching content type isn't found, there's
    a redirect to the browser for an HTML representation.

    :return: None
    """
    response = NodeNegotiator(
        get_parameterized_request(
            Headers({"Accept": "not4realMimetype"}), "aFakesite.com"
        ),
        "kwgr:zipCodeArea.99924",
    ).negotiate()
    assert isinstance(response, RedirectResponse)


def test_negotiate_html() -> None:
    """
    Tests that when HTML is requested, we get a redirect to the browse page

    :return: None
    """
    response = NodeNegotiator(
        get_parameterized_request(
            Headers({"Accept": "text/html"}), "stko-kwg.geog.ucsb.edu/lod/resource/"
        ),
        "kwgr:zipCodeArea.99924",
    ).negotiate()
    assert isinstance(response, RedirectResponse)


@patch("kwg_api.api.node_negotiator.NodeNegotiator._get_rdf")
@pytest.mark.parametrize(
    "mimetype",
    [
        "text/turtle",
        "text/turtle",
        "text/turtle",
        "application/n-triples",
        "application/ld+json",
        "application/rdf+xml",
    ],
)
def test_negotiate_rdf(get_rdf_mock: unittest.mock.MagicMock, mimetype: str) -> None:
    """
    Tests that RDF is requested when asking for RDF formats

    :param mimetype:
    :param get_rdf_mock:
    """
    get_rdf_mock.return_value = None
    NodeNegotiator(
        get_parameterized_request(
            Headers({"Accept": mimetype}), "stko-kwg.geog.ucsb.edu/lod/resource/"
        ),
        "kwgr:zipCodeArea.99924",
    ).negotiate()
    get_rdf_mock.assert_called_once()


@patch("kwg_api.api.node_negotiator.SPARQLWrapper.queryAndConvert")
def test_get_rdf(query_and_convert_mock: unittest.mock.MagicMock) -> None:
    """
    Tests that get_rdf works up to the web request

    :return: None
    """
    negotiator = NodeNegotiator(get_parameterized_request(), "kwgr:zipCodeArea.99924")
    negotiator._get_rdf()
    query_and_convert_mock.assert_called_once()


def test_redirect_browse():
    """
    Tests that
    """
    response = NodeNegotiator(
        get_parameterized_request(
            Headers({"Accept": "text/html"}), "stko-kwg.geog.ucsb.edu/lod/resource/"
        ),
        "kwgr:zipCodeArea.99924",
    )._redirect_browse()
    assert isinstance(response, RedirectResponse)
