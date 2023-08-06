FROM python:3.10

ENV base_address_http=http://stko-kwg.geog.ucsb.edu
ENV base_address_https=https://stko-kwg.geog.ucsb.edu
WORKDIR ./kwg-api/

RUN pip install poetry
RUN poetry config virtualenvs.create false
# Copy the bare minimum to install dependencies. If none of these files have changed,
# the cache is used.
COPY poetry.lock pyproject.toml README.md ./
# Use no-root because the root code folder hasn't been added yet
RUN poetry install --no-root --without dev
COPY kwg_api/ kwg_api/
CMD ["poetry", "run", "start"]
