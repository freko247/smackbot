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
