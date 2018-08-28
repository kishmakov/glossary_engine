hi_map = {'el': 'Καλημέρα.', 'en': 'Good day', 'ru': 'Добрый день.'}
header_map = {'el': 'Ελληνικά.', 'en': 'English', 'ru': 'Русский.'}

def index_context(lang):
    if lang in hi_map:
        return {
            'hi': hi_map[lang],
            'header': header_map[lang],
        }

    return {
        'hi': 'Unknown lang',
        'header': 'Unknown lang',
    }