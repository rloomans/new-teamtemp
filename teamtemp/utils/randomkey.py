#!/usr/bin/env python

from django.utils.crypto import get_random_string

RANDOM_KEY_LEN = 50

def randomkey():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(RANDOM_KEY_LEN, chars)

if __name__ == "__main__":
    print(randomkey())
