from builtins import range
import random
import string


chars = string.ascii_letters + string.digits


def random_string(length):
    return ''.join(random.choice(chars) for _ in range(length))
