import os
from unittest.mock import patch

import pytest

from kwg_api.lib.content_negotiator import ContentNegotiator
from tests.utils.shared_methods import get_parameterized_request


@pytest.fixture
@patch.dict(
    os.environ,
    {
        "base_address_http": "http://stko-kwg.geog.ucsb.edu",
        "base_address_https": "https://stko-kwg.geog.ucsb.edu",
    },
)
def content_fixture() -> ContentNegotiator:
    """
    Fixture that sets up a content negotiator with a test
    Request object.

    :return: A fully constructed ContentNegotiator
    """

    return ContentNegotiator(get_parameterized_request(), "zipcodearea.99924")


def test_init(content_fixture: ContentNegotiator) -> None:
    """
    Tests that key values are being added to the class and
    that the env var is being used for the base address

    :return: None
    """
    assert content_fixture.base_address_http == "http://stko-kwg.geog.ucsb.edu"
    assert content_fixture.base_address_https == "https://stko-kwg.geog.ucsb.edu"
    assert content_fixture.resource_id == "zipcodearea.99924"
    assert (
        str(content_fixture.request_url)
        == "https://stko-kwg.geog.ucsb.edu/lod/resource/"
    )
    assert content_fixture.request_format == "text/turtle"


def test_negotiate_throws(content_fixture) -> None:
    """
    Test that calls to the base negotiate throws

    :return: None
    """
    with pytest.raises(NotImplementedError):
        content_fixture.negotiate()
