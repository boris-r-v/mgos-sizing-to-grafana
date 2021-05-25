FROM python:3.8.5-alpine

LABEL maintainer="borisrozhkin@gmail.com" \
      description="MQTT to InfluxDB Bridge"

COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app

CMD ["python3", "-u", "mqttworker.py"]
