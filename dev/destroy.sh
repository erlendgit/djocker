#!/usr/bin/env bash

docker-compose down -v
docker-compose rm -f
docker image rm -f djocker:0.9
