# syntax=docker/dockerfile:1

FROM python:3.11.7-alpine

WORKDIR /app

COPY . /app

COPY requirements.txt /app

RUN pip install .

COPY run.sh /app

CMD [ "./run.sh" ]

# RUN chmod +x run.sh

# RUN echo "* * * * * /app/run.sh >> /app/logs/cron.log 2>&1" | crontab -