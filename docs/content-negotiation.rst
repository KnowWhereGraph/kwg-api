Content Negotiation
===================
One of the Linked Data principles is that data should be retrievable in different formats, depending on the 'Accept' header, known as Content Negotiation.

KnowWhereGraphs supports content negotiation for graph nodes through the API.

Redirection
-----------
The API will issue 303 redirects when content types are for HTML or otherwise not found.