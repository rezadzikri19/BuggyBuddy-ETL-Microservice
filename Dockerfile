# syntax=docker/dockerfile:1

FROM python:3.11-slim-bullseye

WORKDIR /etl-app

COPY . .

RUN chmod +x *.sh

ENTRYPOINT [ "./entry_point.sh" ]

CMD ["./run.sh"]


