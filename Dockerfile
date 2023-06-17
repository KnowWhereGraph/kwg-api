FROM python:3.10

ENV base_address=http://localhost
WORKDIR ./kwg-api/

COPY ./requirements.txt requirements.txt
COPY ./src ./src
RUN pip install --upgrade -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]