import logging

import wikipedia


def wiki_summary(query):
    try:
        summary = wikipedia.summary(query)
        span = 3
        summary_parts = summary.split('. ')
        return [('. '.join(summary_parts[i:i+span])+'.').encode('utf-8')
                for i in range(0, len(summary_parts), span)]
    except wikipedia.exceptions.DisambiguationError as e:
        return 'Disambiguation:\n'+'\n'.join(e.options)


def wiki_search(query):
    try:
        page_id = wikipedia.search(query)
        if page_id:
            page = wikipedia.page(page_id[0])
            return (page.summary.split('. ')[0] + '.\n' + page.url).encode('utf-8')
    except wikipedia.exceptions.PageError:
        logging.exception('Could not retrieve Wiki')
        return None
