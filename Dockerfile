FROM python:3.8-slim

ENV LANG=C.UTF-8

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
ARG PORT
ENV FLET_SERVER_PORT=$PORT

EXPOSE $PORT


CMD ["python", "./app/app.py"]