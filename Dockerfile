FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./caishen_dashboard /app/caishen_dashboard
COPY run_dashboard.py /app/

EXPOSE 8050

ENTRYPOINT ["python", "run_dashboard.py"]
#CMD [ "gunicorn", "--workers=1", "--threads=1", "-b 0.0.0.0:8050", "caishen_dashboard.server:server"]