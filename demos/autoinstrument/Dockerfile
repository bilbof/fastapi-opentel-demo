FROM python:alpine3.15

RUN pip install fastapi uvicorn
RUN pip install opentelemetry-distro==0.32b0 opentelemetry-sdk==1.12.0rc2 opentelemetry-api==1.12.0rc2
COPY app.py .
RUN opentelemetry-bootstrap --action=install

ENV WORKERS=1

CMD opentelemetry-instrument \
    --traces_exporter=console \
    --log_level=debug \
    --logs_exporter=console \
    --metrics_exporter=none \
    uvicorn \
    app:app \
    --host=0.0.0.0 \
    --workers=${WORKERS}
