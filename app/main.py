from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest
import time

app = FastAPI()

# Лічильник запитів (по методу, шляху, статусу)
HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"]
)

# Час відповіді (latency) у секундах
HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "path"]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start

    path = request.url.path
    method = request.method
    status = str(response.status_code)

    HTTP_REQUESTS_TOTAL.labels(method=method, path=path, status=status).inc()
    HTTP_REQUEST_DURATION_SECONDS.labels(method=method, path=path).observe(duration)

    return response

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps Intern 👋"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/slow")
def slow():
    time.sleep(0.8)
    return {"status": "slow response"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")