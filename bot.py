import logging

from quotes import qod
from wiki import wiki_summary, wiki_search

def reader(message):
    commands = {'/qod': qod,
                '/ping': lambda x: 'pong',
                '/wiki': wiki_search,
                '/wiki_summary': wiki_summary
                }
    if message.startswith('/'):
        try:
            command = commands[message.split()[0]]
            return command(' '.join(message.split()[1:])) or message
        except:
            logging.exception('Could not execute command: %s' % message)
            return message
    else:
        return None
