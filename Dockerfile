# syntax=docker/dockerfile:1

FROM python:3.10-alpine3.18

RUN apk update && \
  apk add --no-cache bash && \
  apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers && \
  apk add --no-cache libffi-dev openssl-dev && \
  apk add --no-cache rust cargo

WORKDIR /app

COPY . /app

COPY requirements.txt /app

COPY *.sh /app

RUN chmod +x *.sh

ENTRYPOINT ["./entry_point.sh"]

CMD [ "./run.sh" ]

# RUN echo "* * * * * /app/run.sh >> /app/logs/cron.log 2>&1" | crontab -