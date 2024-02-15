# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends bash && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get install -y --no-install-recommends libffi-dev openssl && \
    apt-get install -y --no-install-recommends rustc cargo && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN chmod +x /app/*.sh

ENTRYPOINT ["./entry_point.sh"]

# CMD [ "./run.sh" ]

# RUN echo "* * * * * /app/run.sh >> /app/logs/cron.log 2>&1" | crontab -