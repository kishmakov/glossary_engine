from server.localizations import localizations

LANG_ID = 0
HI_ID = 1
LIST_ID = 2


def index_context(lang, index):
    authors = []
    for author_id, author_name in index['authors'].items():
        authors.append({'id': author_id, 'name': author_name})

    context = localizations[lang]
    context['authors'] = authors
    context['lang'] = lang
    context['header'] = context['loc_project_name']

    return context


def author_context(lang, index, author_id):
    context = localizations[lang]
    context['author'] = {'name': index['authors'][author_id], 'id': author_id}
    context['lang'] = lang
    context['header'] = index['authors'][author_id]
    context['texts'] = index[author_id]

    return context