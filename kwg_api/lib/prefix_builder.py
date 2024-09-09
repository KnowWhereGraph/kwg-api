import json
import logging
import os
from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader
from starlette.datastructures import URL

logger = logging.getLogger(__name__)


class PrefixBuilder:
    """
    Build a JSON document with the prefixes used by KnowWhereGraph
    """

    def __init__(self):
        pass

    @staticmethod
    def build() -> Dict[str, str]:
        """
        Builds the prefix dictionary by loading the vocabulary
        from disk and inserting the base address into it.

        :return: A dictionary of { vocab location: prefix}
        """
        file_loader = FileSystemLoader("")
        env = Environment(loader=file_loader)
        template = env.get_template("kwg_api/resources/vocabulary.json")
        context = template.render(
            base_kwg_url_http=os.environ.get("base_address_http"),
            base_kwg_url_https=os.environ.get("base_address_https"),
        )
        return json.loads(context)

    @staticmethod
    def resolve_prefix(full_uri: str | URL, resource_id: str) -> str | None:
        """
        Given a full node URI, replace as much as the URI as possible with a prefix.
        The trick is to
        1. Determine the prefix by finding whether the URI is describing a resource,
         or an ontology item
        2. Use the resource id

        :param full_uri: The full URI path
        :param resource_id: The end of the URI that appears post-prefix. eg kwg:resource_id
        :return: The URI, prefixed or None
        """
        # Get the supported prefixes
        vocab = PrefixBuilder().build()
        try:
            # Split the resource out of the . It should look like
            # {base_address}/lod/resource/
            base_url = str(full_uri).split(resource_id)[0]
        except IndexError:
            logging.warning(
                f"Failed to find a prefix for URI {full_uri}", exc_info=True
            )
            return None
        try:
            # Find the prefix (key) whose full path (value) matches
            return f"{vocab[base_url]}:{resource_id}"
        except KeyError:
            logging.warning(
                f"Failed to find a matching prefix for {full_uri}.", exc_info=True
            )
        return None
