hi_map = {'el': 'Καλημέρα.', 'en': 'Good day', 'ru': 'Добрый день.'}
header_map = {'el': 'Ελληνικά.', 'en': 'English', 'ru': 'Русский.'}

def index_context(lang, index):
    authors = []
    for author_id in index['authors']:
        authors.append({'id': author_id, 'name': index['authors'][author_id]})

    return {
        'hi': hi_map[lang],
        'header': header_map[lang],
        'lang': lang,
        'authors': authors
    }

