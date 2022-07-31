## OpenTelemetry FastAPI autoinstrumentation demo

This demos how to auto-instrument a Fast API application (uvicorn).

```bash
docker build -t uvicorn-demo .
docker run -it -p 8000:8000 uvicorn-demo
```

Visit http://localhost:8000/items/5?q=somequery

Look in the application logs for OpenTelemetry traces (wait a few seconds).
Example:

```json
{
    "name": "/items/{item_id}",
    "context": {
        "trace_id": "0xea16ca9099c4f0727308c083fd207465",
        "span_id": "0xe7f33889d53a3436",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2022-07-23T19:33:08.117173Z",
    "end_time": "2022-07-23T19:33:08.122356Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.scheme": "http",
        "http.host": "172.17.0.3:8000",
        "net.host.port": 8000,
        "http.flavor": "1.1",
        "http.target": "/items/5",
        "http.url": "http://172.17.0.3:8000/items/5?q=somequery",
        "http.method": "GET",
        "http.server_name": "localhost:8000",
        "net.peer.ip": "172.17.0.1",
        "net.peer.port": 55296,
        "http.route": "/items/{item_id}",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "telemetry.auto.version": "0.32b0",
        "service.name": "unknown_service"
    }
}
```
