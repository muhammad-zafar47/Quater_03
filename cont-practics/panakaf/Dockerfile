FROM python:3.12

LABEL maintance="panacloudpk"

WORKDIR /code

COPY . /code/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

CMD poetry run uvicorn app.main:app --reload 