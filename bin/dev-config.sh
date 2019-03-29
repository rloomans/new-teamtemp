#!/bin/bash

sudo dnf install python3-devel
virtualenv env --python=python3
source env/bin/activate
pip install -Ur requirements/base.txt
pip install -Ur requirements/dev.txt
pip install -U psycopg2-binary
export TEAMTEMP_SECRET_KEY=$(date -Ins)-$(hostname)
# 2018-05-07T17:29:18,478477185+10:00-loonatix.atom.inc
export PYTHONPATH=$(pwd)/teamtemp
export DJANGO_SETTINGS_MODULE=teamtemp.settings.dev
./manage.py collectstatic
./manage.py migrate
./manage.py runserver

