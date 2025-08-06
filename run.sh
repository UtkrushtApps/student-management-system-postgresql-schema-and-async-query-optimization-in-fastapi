#!/bin/bash
set -e
cd /root/task
echo "Starting docker containers..."
docker-compose up -d
# Wait for postgres
echo "Waiting for PostgreSQL to become available..."
RETRIES=0
until docker exec $(docker-compose ps -q postgres) pg_isready -U student_user -d student_db; do
  sleep 2
  RETRIES=$((RETRIES+1))
  if [ $RETRIES -gt 30 ]; then
    echo "PostgreSQL did not become available in time."
    exit 1
  fi
done
echo "PostgreSQL is ready."
sleep 5
# FastAPI health check
OK=false
for i in {1..12}; do
  if curl -s http://localhost:8000/docs > /dev/null; then
    OK=true
    break
  fi
  sleep 2
done
if [ "$OK" = false ]; then
  echo "Error: FastAPI application did not become responsive."
  exit 1
fi
echo "FastAPI application is running and connected."
docker-compose ps
