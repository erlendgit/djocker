#!/usr/bin/env bash

docker-compose down -v
docker-compose rm -f
docker rmi -f djocker:latest
