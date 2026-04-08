# DevOps Mini API Monitoring

A small demo project for monitoring a FastAPI service using **Prometheus + Grafana + Docker Compose**.

---

## Use cases

This project simulates a real-world monitoring setup where:

- API traffic is tracked in real time  
- Slow endpoints can be detected via latency metrics  
- Request rates help identify load spikes  
- Dashboards provide quick operational insights  

---

## Features

- FastAPI application  
- Prometheus metrics (`/metrics`)  
- Request counter & latency (Histogram)  
- Grafana dashboards  
- Fully dockerized setup  
- Simulated slow endpoint (`/slow`) for latency testing  

---

## Tech Stack

- Python (FastAPI)  
- Prometheus  
- Grafana  
- Docker / Docker Compose  

---

## Project Structure

```bash
.
├── app/
│   ├── main.py
│   └── requirements.txt
├── infra/
│   └── prometheus/
│       └── prometheus.yml
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Quick Start

```bash
git clone https://github.com/nsavenokk/devops-mini-api-monitoring.git
cd devops-mini-api-monitoring
docker compose up --build
```

---

## Endpoints

- API → http://localhost:8000  
- Swagger → http://localhost:8000/docs  
- Metrics → http://localhost:8000/metrics  
- Grafana → http://localhost:3000  

Login: **admin / admin**

---

## Grafana Dashboards

- API Requests per Second  
- Total Requests by Path  
- P95 Latency by Endpoint  

---

## Example requests

```bash
curl http://localhost:8000/
curl http://localhost:8000/slow
```

---

## Demo

Example Grafana dashboard:

![Grafana Dashboard](screenshots/dashboard.png)

---

## Example Prometheus Queries

### Requests per second

```promql
sum(rate(http_requests_total{path!="/metrics", path!="/favicon.ico"}[$__rate_interval]))
```

### Total requests by path

```promql
sum by (path) (http_requests_total{path!="/metrics", path!="/favicon.ico"})
```

### P95 latency

```promql
histogram_quantile(
  0.95,
  sum(rate(http_request_duration_seconds_bucket{path!="/metrics", path!="/favicon.ico"}[$__rate_interval])) by (le, path)
)
```

---

## What I learned

- How to instrument FastAPI with Prometheus  
- How Prometheus collects and stores metrics  
- How to build Grafana dashboards  
- How to monitor latency (P95)  
- How to run a monitoring stack using Docker  

---

## Why this project matters

This project demonstrates:

- Observability basics  
- Metrics collection & visualization  
- Prometheus + Grafana integration  
- Containerized infrastructure  
- Real-world DevOps workflow  

---

## Author

**Anastasiia Savenok**
