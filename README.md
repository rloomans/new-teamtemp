new-teamtemp
============

[![Build Status](https://travis-ci.org/rloomans/new-teamtemp.svg)](https://travis-ci.org/rloomans/new-teamtemp)
[![Coverage Status](https://coveralls.io/repos/rloomans/new-teamtemp/badge.svg?branch=master&service=github)](https://coveralls.io/github/rloomans/new-teamtemp?branch=master)
[![Codecov](https://img.shields.io/codecov/c/github/rloomans/new-teamtemp/master.svg?maxAge=2592000)](http://codecov.io/github/rloomans/new-teamtemp?branch=master)
[![Code Climate](https://codeclimate.com/github/rloomans/new-teamtemp/badges/gpa.svg)](https://codeclimate.com/github/rloomans/new-teamtemp)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&identifier=51559407)](https://dependabot.com)

This application is designed to gather 'team temperature' - that is, a
happiness score.

For the sake of security, very little information is stored or recorded. Each
submitter is represented by a random ID, and a cookie is stored so really only
to protect against accidental double submissions from the same user with the
same browser.

The results page are available to the creator using the same cookie mechanism,
and also a password in case the cookie is lost.

