FROM python:3.6

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

RUN apt-get install libcairo2-dev
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.create_app:create_app()"