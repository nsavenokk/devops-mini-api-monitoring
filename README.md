# DevOps Mini API Monitoring

Small demo project for monitoring a FastAPI service using **Prometheus + Grafana + Docker**.

---

## Features

* FastAPI application
* Prometheus metrics (`/metrics`)
* Request counter & latency (Histogram)
* Grafana dashboards
* Docker & Docker Compose setup

---

## Tech Stack

* Python (FastAPI)
* Prometheus
* Grafana
* Docker / Docker Compose

---

## Run project

```bash
docker compose up --build
```

---

## Endpoints

* API: http://localhost:8000
* Metrics: http://localhost:8000/metrics
* Grafana: http://localhost:3000

---

## Grafana Dashboards

Project includes:

* API Requests per Second
* Total Requests by Path
* P95 Latency by Endpoint

---

## Example requests

```bash
curl http://localhost:8000/
curl http://localhost:8000/slow
```

---

## Demo

*Add your Grafana screenshot here*

---

## 💡 What I learned

* How to expose Prometheus metrics in FastAPI
* How to visualize metrics in Grafana
* How to run monitoring stack using Docker
* Basics of DevOps monitoring

---

## 👩‍💻 Author

Anastasiia Savenok
