FROM python:3.10

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
# Copy the bare minimum to install dependencies. If none of these files have changed,
# the cache is used.
COPY poetry.lock pyproject.toml README.md ./
# Use no-root because the root code folder hasn't been added yet
RUN poetry install --no-root --without dev
COPY . .

CMD ["poetry", "run", "uvicorn", "kwg_api.main:app", "--host", "0.0.0.0", "--port", "8080"]
