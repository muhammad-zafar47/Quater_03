
From python:3.12

LABEL maintainer="zafarch"

WORKDIR /code

COPY . /code/

RUN pip install poetry 

RUN poetry config virtualenvs.create false

RUN poetry install

CMD poetry run uvicorn hello.main:app --reload