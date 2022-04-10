#!/usr/bin/env bash

./dev/abort.sh
./dev/destroy.sh

docker-compose build

./dev/up.sh

docker-compose exec web python manage.py migrate