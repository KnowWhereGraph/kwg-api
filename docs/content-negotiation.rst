Content Negotiation
===================
One of the Linked Data principles is that data should be retrievable in different formats, depending on
the 'Accept' header, known as [Content Negotiation](https://en.wikipedia.org/wiki/Content_negotiation).

KnowWhereGraphs supports content negotiation for graph nodes through the API.

Examples
-------

Python
______
.. code-block:: python
    import requests

    requests.get("stko.kwg.geog.ucsb.edu/lod/ontology/)


curl
____

.. code-block:: bash
    curl .....

Redirection
-----------
The API will issue 303 redirects when content types are for HTML or otherwise not found.