#!/bin/bash
# Script to run Turl's backend and frontend
trap "exit" INT TERM ERR
trap "kill 0" EXIT

cd backend/turl
python3 manage.py migrate
python3 manage.py runserver &
cd ..
cd ..
cd frontend
npm i
ng serve --open
wait