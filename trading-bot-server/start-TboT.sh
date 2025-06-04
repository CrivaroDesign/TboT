#!/bin/bash
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > logs/server.log 2>&1 &
echo "Trading bot running in background..."