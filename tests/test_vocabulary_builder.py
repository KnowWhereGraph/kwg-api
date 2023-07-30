import os
import unittest.mock
from unittest.mock import patch

import pytest

from kwg_api.lib.prefix_builder import PrefixBuilder


def test_init() -> None:
    """
    Tests that construction works

    :return: None
    """
    builder = PrefixBuilder()
    assert builder


@patch.dict(
    os.environ,
    {
        "base_address_http": "http://stko-kwg.geog.ucsb.edu",
        "base_address_https": "https://stko-kwg.geog.ucsb.edu",
    },
)
def test_build() -> None:
    """
    Tests that the builder is creating a dictionary using
    the environment's base address.

    :return: None
    """
    prefixes = PrefixBuilder.build()
    assert prefixes["http://stko-kwg.geog.ucsb.edu/lod/ontology/"]
    assert prefixes["https://stko-kwg.geog.ucsb.edu/lod/ontology/"]


@pytest.mark.parametrize(
    "full_uri, resource_uri, expected_prefix",
    [
        [
            "http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion_2",
            "AdministrativeRegion_2",
            "kwg-ont",
        ],
        [
            "http://stko-kwg.geog.ucsb.edu/lod/ontology/NOAAHeavySnow",
            "NOAAHeavySnow",
            "kwg-ont",
        ],
        ["http://stko-kwg.geog.ucsb.edu/lod/ontology/Hazard", "Hazard", "kwg-ont"],
        [
            "http://stko-kwg.geog.ucsb.edu/lod/resource/hazard.1183609.5434007",
            "hazard.1183609.5434007",
            "kwgr",
        ],
        [
            "http://stko-kwg.geog.ucsb.edu/lod/resource/instant.200502140700MST",
            "instant.200502140700MST",
            "kwgr",
        ],
        ["http://stko-kwg.geog.ucsb.edu/lod/lite-ontology/", "Place", "kwgl-ont"],
        [
            "http://stko-kwg.geog.ucsb.edu/lod/lite-ontology/hasMappingProgram",
            "hasMappingProgram",
            "kwgl-ont",
        ],
        [
            "https://stko-kwg.geog.ucsb.edu/lod/lite-resource/nwzone.30034",
            "nwzone.30034",
            "kwglr",
        ],
        [
            "https://stko-kwg.geog.ucsb.edu/lod/lite-resource/Earth.North_America.United_States.USA.2_1",
            "Earth.North_America.United_States.USA.2_1",
            "kwglr",
        ],
    ],
)
@patch.dict(
    os.environ,
    {
        "base_address_http": "http://stko-kwg.geog.ucsb.edu",
        "base_address_https": "https://stko-kwg.geog.ucsb.edu",
    },
)
def test_resolve_prefix(full_uri, resource_uri, expected_prefix) -> None:
    """
    Test that the correct prefixes are being created for commonly used
    paths.

    :return: None
    """
    prefixed = PrefixBuilder.resolve_prefix(full_uri, resource_uri)
    assert prefixed == f"{expected_prefix}:{resource_uri}"


@patch.dict(
    os.environ,
    {
        "base_address_http": "http://stko-kwg.geog.ucsb.edu",
        "base_address_https": "https://stko-kwg.geog.ucsb.edu",
    },
)
def test_resolve_prefix_not_found() -> None:
    """
    Test that when a prefix wasn't found, None is returned.

    :return: None
    """
    shortened_prefix = PrefixBuilder.resolve_prefix("notARealResource", "123")
    assert not shortened_prefix
