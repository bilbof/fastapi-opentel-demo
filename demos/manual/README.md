## OpenTelemetry FastAPI autoinstrumentation demo

This demos how to instrument a Fast API application manually.

```bash
docker build -t fastapi-demo-manual .
docker run -it -p 8000:8000 fastapi-demo-manual
```

Visit http://localhost:8000/fib/3

Look in the application logs for OpenTelemetry traces.

Visit http://localhost:8000/fiboverhttp/3 which includes an instrumented call to itself.

### Example `/fib/2` call trace:

Note each object is a span. fib-n are custom spans.
`/fib/{number} http send` spans are created by monkey-patching the requests library.
`/fib/{number}` spans are created by monkey-patching the fastapi library.

```json
{
    "name": "fib-0",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0xd0f1658113577841",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xd4c19690b1a6c501",
    "start_time": "2022-07-26T22:27:42.026846Z",
    "end_time": "2022-07-26T22:27:42.026915Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
{
    "name": "fib-1",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0xbbce3f7a16a68ccb",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xd4c19690b1a6c501",
    "start_time": "2022-07-26T22:27:42.027220Z",
    "end_time": "2022-07-26T22:27:42.027239Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
{
    "name": "fib-2",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0xd4c19690b1a6c501",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xc0d90c76b6841c4a",
    "start_time": "2022-07-26T22:27:42.026733Z",
    "end_time": "2022-07-26T22:27:42.027257Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
{
    "name": "/fib/{number} http send",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0x7600e7b852480e04",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xc0d90c76b6841c4a",
    "start_time": "2022-07-26T22:27:42.027496Z",
    "end_time": "2022-07-26T22:27:42.028167Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.status_code": 200,
        "type": "http.response.start"
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
{
    "name": "/fib/{number} http send",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0x2968ee04ca45fc4e",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xc0d90c76b6841c4a",
    "start_time": "2022-07-26T22:27:42.028253Z",
    "end_time": "2022-07-26T22:27:42.028655Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "type": "http.response.body"
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
{
    "name": "/fib/{number}",
    "context": {
        "trace_id": "0xed4b681b04c6a22f684c5b30d8a9798f",
        "span_id": "0xc0d90c76b6841c4a",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2022-07-26T22:27:42.026131Z",
    "end_time": "2022-07-26T22:27:42.028727Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.scheme": "http",
        "http.host": "172.17.0.3:8000",
        "net.host.port": 8000,
        "http.flavor": "1.1",
        "http.target": "/fib/2",
        "http.url": "http://172.17.0.3:8000/fib/2",
        "http.method": "GET",
        "http.server_name": "127.0.0.1:8000",
        "net.peer.ip": "172.17.0.1",
        "net.peer.port": 55850,
        "http.route": "/fib/{number}",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "1.12.0rc2",
        "service.name": "demo-app",
        "telemetry.auto.version": "0.32b0"
    }
}
```
