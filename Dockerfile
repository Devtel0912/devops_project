FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app

CMD [ "python","app/main.py" ]

