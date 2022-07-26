FROM python:alpine3.15

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV OTEL_LOG_LEVEL=debug
ENV OTEL_METRICS_EXPORTER=none
ENV OTEL_TRACES_EXPORTER=console
ENV OTEL_LOGS_EXPORTER=console
ENV OTEL_PROPAGATORS=tracecontext,baggage
ENV OTEL_PYTHON_LOG_CORRELATION=true
ENV OTEL_SERVICE_NAME=demo-app

CMD [ \
  "opentelemetry-instrument", \
  "uvicorn", \
  "app:app", \
  "--host=0.0.0.0",\
  "--port=8000"]
