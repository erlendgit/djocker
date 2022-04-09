#!/usr/bin/env bash

./dev/abort.sh
./dev/destroy.sh

docker-compose build

./dev/up.sh