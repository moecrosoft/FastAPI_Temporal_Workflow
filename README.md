# Temporal + FastAPI Workflow

This repo creates FastAPI apis and connect them to temporal server to execute workflows. FastAPI server is connected in local host, temporal server is run in docker compose but is pointed to localhost. Api requests can be sent from command line to start workflow or query workflow progress.

ChatGPT is utilized to learn about FastAPI, Temporal and Docker. It is also utilized to learn how to build workers,workflows,activites and for debugging.

---

## Prerequisites

- Python 3+
- Docker & Docker Compose
- `pip` (Python package manager)

---

## 1. Clone the repository

```
git clone <repo-url>
cd temporal
```


## 2. Start virtual environment
```
python -m venv venv  
source venv/bin/activate  (macOS/Linux)
or
venv\Scripts\activate      (Windows)
```

## 3. Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Start Temporal server in docker compose
```
docker-compose up -d
```

## 5. Check if the Temporal server is running
```
docker ps
```

## 6. Activate the Temporal worker on standby
```
python worker/worker.py
```

## 7. Start the FastAPI server
```
uvicorn api.main:app --reload
```

## 8. Send a post request with json to start workflow
```
curl -X POST http://127.0.0.1:8000/jobs \
-H "Content-Type: application/json" \
-d '{"input":{"numbers":[1,2,3,4]},"options":{"fail_first_attempt":true}}'
```

## 9. Send a get request to query the workflow progress
```
curl http://127.0.0.1:8000/jobs/job-<id>
```
---

## Output in VSCode terminal

![output.jpg]
