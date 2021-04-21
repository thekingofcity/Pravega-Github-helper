import re
import ctypes
import json
from typing import Dict, Any

import requests


def Mbox(title: str, text: str, style: int = 1) -> bool:
    return True if ctypes.windll.user32.MessageBoxW(0, text, title,
                                                    style) == 1 else False


def get_issue(issue_url: str) -> Dict[str, Any]:
    location = re.match(r'https://github.com/(\S+/\S+/issues/\d+)', issue_url)
    if not location:
        raise RuntimeError('Not a valid github issue')

    api = f'https://api.github.com/repos/{location.group(1)}'

    r = requests.get(api, headers={'Accept': 'application/vnd.github.v3+json'})

    return json.loads(r.text)
