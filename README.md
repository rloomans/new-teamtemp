new-teamtemp
============

[![Django Test Status](https://github.com/rloomans/new-teamtemp/actions/workflows/django-test.yaml/badge.svg?branch=main)](https://github.com/rloomans/new-teamtemp/actions/workflows/django-test.yaml)
[![Coverage Status](https://coveralls.io/repos/rloomans/new-teamtemp/badge.svg?branch=main&service=github)](https://coveralls.io/github/rloomans/new-teamtemp?branch=main)
[![codecov](https://codecov.io/gh/rloomans/new-teamtemp/branch/main/graph/badge.svg)](https://codecov.io/gh/rloomans/new-teamtemp)

This application is designed to gather 'team temperature' - that is, a
happiness score.

For the sake of security, very little information is stored or recorded. Each
submitter is represented by a random ID, and a cookie is stored so really only
to protect against accidental double submissions from the same user with the
same browser.

The results page are available to the creator using the same cookie mechanism,
and also a password in case the cookie is lost.


Heroku One-click Deploy
-----------------------

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

After you successfully deploy your app to Heroku, make sure that you add the following to the Heroku Scheduler as a daily job:

```
python bin/archive_scores.py
```

Also, if you want to access the Django admin site, add a super user using the heroku CLI:

```
heroku run --app <Your Heroku app name here> python manage.py createsuperuser --username <admin user> --email <admin email address>
```

and then go to `https://<Your Heroku app name here>.herokuapp.com/djadmin/`

