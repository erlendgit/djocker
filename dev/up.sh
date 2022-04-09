#!/usr/bin/env bash

docker-compose pull
docker-compose build
docker-compose up -d
docker-compose exec web pip freeze
docker-compose exec web /bin/bash