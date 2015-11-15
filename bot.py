import logging

from quotes import qod


def reader(message):
    commands = {'/qod': qod
                }
    if message.startswith('/'):
        try:
            command = commands[message.split()[0]]
            return command() or message
        except:
            logging.exception('Could not execute command: %s' % message)
            return message
