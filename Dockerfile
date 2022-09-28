FROM python:3.9-slim

ENV CONTAINER_HOME=/var/www
WORKDIR ${CONTAINER_HOME}
COPY requirements.txt ${CONTAINER_HOME}
RUN apt update && apt install -y procps
RUN mkdir -p /tobeanalyzed
RUN mkdir -p /tobestored
RUN python -m pip install --upgrade pip && pip install -r $CONTAINER_HOME/requirements.txt