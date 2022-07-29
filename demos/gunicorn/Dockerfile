FROM python:alpine3.15

RUN pip install fastapi uvicorn gunicorn opentelemetry-distro
COPY app.py .
RUN opentelemetry-bootstrap --action=install

CMD [ \
  "opentelemetry-instrument", \
  "--traces_exporter=console", \
  "--log_level=debug", \
  "--logs_exporter=console", \
  "--metrics_exporter=none", \
  "gunicorn", \
  "app:app", \
  "-b=0.0.0.0:8000", \
  "-k uvicorn.workers.UvicornWorker", \
  "-w 4"]
