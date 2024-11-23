# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gberg.wsgi:application"]
