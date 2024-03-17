#! /usr/bin/env bash
set -e

python -m alembic upgrade head
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
