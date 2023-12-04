FROM python:3.9.6-alpine

RUN apk update && apk add gcc python3-dev musl-dev

RUN mkdir -p /opt/app

WORKDIR /opt/app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY db_service.py db_service.py
COPY consumer.py consumer.py

CMD ["python", "./consumer.py"]