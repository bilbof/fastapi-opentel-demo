FROM python:alpine3.15

RUN pip install fastapi uvicorn
RUN pip install opentelemetry-distro
COPY app.py .
RUN opentelemetry-bootstrap --action=install

CMD [ \
  "opentelemetry-instrument", \
  "--traces_exporter=console", \
  "--log_level=debug", \
  "--logs_exporter=console", \
  "--metrics_exporter=none", \
  "uvicorn", \
  "app:app", \
  "--host=0.0.0.0"]
