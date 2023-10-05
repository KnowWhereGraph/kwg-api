Developing
==========


Adding New Endpoints
--------------------
New endpoints should be added to `kwg_api/main.py`. Each endpoint should have its code located in a new class, in the `kwg_api/api/*`
folder. The class and new method in main.py should have associated unit tests.

Adding New API Versions
-----------------------
Version changes should follow [Semantic Versioning] guidelines. GitHub's version feature should also
be used to tag & release the new version. Version releases should be auto-generated from commit logs with any
additional information that may be helpful for users (breaking changes, usability improvements, etc).

Adding New Content Negotiation Formats
--------------------------------------
If nodes are supporting new return formats, the easiest way to add this
is in the NodeNegotiator class by mapping the new mimetype to the RDFLib
return type.

Adding new library items
------------------------
New library items belong in `kwg_api/lib` and should be accompanied by unit tests.

Code Style
----------

The style should conform to the black tool. Linting is automated through poetry. Refer to the README for instructions on running. Specific parameters and new linters can be added in `pyproject.toml`.
