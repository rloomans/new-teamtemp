from builtins import range
import random
import string
import json


chars = string.ascii_letters + string.digits


def random_string(length):
    return ''.join(random.choice(chars) for _ in range(length))


def filter_csp_report(request):
    report = json_str = request.body
    if isinstance(json_str, bytes):
        json_str = json_str.decode(request.encoding or 'utf-8')
    report = json.loads(request.body)
    src_file = report.get('csp-report', {}).get('source-file', '')
    ignored_prefixes = (
        'safari-extension://',
        'safari-web-extension://',
        'moz-extension://',
        'chrome-extension://',
    )
    if any(src_file.startswith(prefix) for prefix in ignored_prefixes):
        return False
    return True

