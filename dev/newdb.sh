#!/usr/bin/env bash

rm ./project/db.sqlite3 -f
sqlite3 ./project/db.sqlite3 "VACUUM;"
./dev/rebuild.sh
./dev/cmd.sh migrate
