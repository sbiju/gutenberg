FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gberg.wsgi:application"]
