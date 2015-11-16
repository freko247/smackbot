# -*- coding:utf-8 -*- 
import logging

from quotes import qod
from wiki import wiki_summary, wiki_search
from settings import interactions

def commander(message):
    commands = {'/qod': qod,
                '/ping': lambda x: 'pong',
                '/wiki': wiki_search,
                '/wiki_summary': wiki_summary
                }
    try:
        command = commands[message.split()[0]]
        return command(' '.join(message.split()[1:])) or message
    except:
        logging.exception('Could not execute command: %s' % message)
        return message


def scan_and_react(message):
    set_reactions = []
    reaction_text = ''
    print type(message)
    for key in interactions.keys():
        print key.encode('utf-8')
        enc = key.encode('utf-8')
        if enc in message.lower():
            reaction = interactions[key]
            if reaction not in set_reactions:
                reaction_text += ' '+reaction.encode('utf-8')
                set_reactions.append(reaction)
    return reaction_text

def reader(message):
    if message.startswith('/'):
        return reader(message)
    else:
        return scan_and_react(message)
