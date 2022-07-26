from typing import Union
from fastapi import FastAPI
import uvicorn

import random
import requests
from opentelemetry import trace

app = FastAPI()

MAX_FIB=10

def fib(n):
    # Custom trace example:
    with trace.get_tracer(__name__).start_as_current_span(f"fib-{n}"):
      if n < 2:
          return n
      return fib(n-2) + fib(n-1)

def fib_api_call(n):
    print("making api call")
    return requests.get(f"http://0.0.0.0:8000/fib/{n}", timeout=1)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fib")
async def read_fibonacci_rand():
    number = random.randint(1,MAX_FIB)
    return { "number": number, "answer": fib(number) }

@app.get("/fib/{number}")
async def read_fibonacci_number(number: int):
    print("received api call")
    number = min(number,MAX_FIB)
    return { "number": number, "answer": fib(number) }

@app.get("/fiboverhttp/{number}")
def read_fibonacci_over_http(number: int):
    res = fib_api_call(number)
    if res.ok:
      return res.json()
    return { "error": res.text }
