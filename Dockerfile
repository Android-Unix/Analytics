FROM python:3.11.3-slim

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project dependencies
COPY ./requirements.txt app/requirements.txt

# Copy dev dependencies
COPY ./requirements-dev.txt app/requirements-dev.txt

# Run project dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Run dev dependencies
RUN pip install --no-cache-dir -r app/requirements-dev.txt

COPY . .

EXPOSE 8000
