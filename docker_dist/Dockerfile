FROM python:3.8-buster
ARG port

WORKDIR /app

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY wsgi.py ./
COPY docker_dist/boot.sh ./
COPY config.py ./
COPY ./caishen_dashboard /app/caishen_dashboard

EXPOSE $port

# fix line endings and allow to run as executable
RUN sed -i 's/\r$//' boot.sh  && chmod +x boot.sh

ENTRYPOINT []
