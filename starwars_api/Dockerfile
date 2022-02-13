FROM python:3.10-slim

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . .

RUN pip install -e .

CMD ["gunicorn", "--bind=0.0.0.0:8000", "--timeout", "50", "starwars.wsgi", "--workers", "4"]