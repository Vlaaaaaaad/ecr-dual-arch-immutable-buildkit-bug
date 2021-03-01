FROM python:3.9

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN POETRY_VIRTUALENVS_IN_PROJECT=true poetry install --no-dev

COPY . .

EXPOSE 5002
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "-b0.0.0.0:5002", "app:app"]
