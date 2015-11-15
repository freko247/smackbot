import json
import logging

import requests


def qod():
    url = 'http://api.theysaidso.com/qod'
    response = requests.get(url)
    try:
        if response.status_code == 200:
            quote = response.json()
            return '%(quote)s - %(author)s' % quote['contents'][0]
        else:
            logging.warning(response.reason)
            return None
    except Exception:
        logging.exception('Could not successfully retriev quote!')
