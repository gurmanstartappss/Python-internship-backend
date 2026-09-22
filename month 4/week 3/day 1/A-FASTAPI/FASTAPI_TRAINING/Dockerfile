FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt requirements.txt

COPY . .
EXPOSE 8080
CMD["uvicorn"]