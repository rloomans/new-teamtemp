#!/usr/bin/env python
import os
import sys

import requests

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamtemp.settings")

    url = os.environ.get('TEAM_TEMP_CRON_URL', 'http://127.0.0.1:8000/cron/')
    pin = os.environ.get('TEAM_TEMP_CRON_PIN', '0000')

    r = requests.get(url + pin)

    if (r.status_code == 200):
        sys.exit(0)

    print(r)
    sys.exit(10)
