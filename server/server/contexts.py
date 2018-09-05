from django.http import Http404

from server.localizations import localizations

from index_el import index as index_el
from index_en import index as index_en
from index_ru import index as index_ru


indexes = {
    'el': index_el,
    'en': index_en,
    'ru': index_ru,
}


def _get_lang_context(lang):
    if lang not in localizations:
        raise Http404('Requested lang "{0}" is not supported.'.format(lang))

    context = localizations[lang]
    context['lang'] = lang
    return context, indexes[lang]


def _get_author(index, author_id):
    for author in index['authors']:
        if author['id'] == author_id:
            return author

    raise Http404('Requested author "{0}" is not found.'.format(author_id))

def _get_text(index, author_id, text_id):
    if author_id not in index['texts']:
        raise Http404('Requested author "{0}" is not found.'.format(author_id))

    for text in index['texts'][author_id]:
        if text['id'] == text_id:
            return text

    raise Http404('Requested text "{0}" is not found for author "{1}".'.format(text_id, author_id))



def language_context():
    langs = []
    for code, lc in sorted(localizations.items()):
        langs.append({'code': code, 'selfname': lc['loc_selfname'], 'flag': lc['loc_flag']})
    return {'langs': langs}


def index_context(lang):
    context, index = _get_lang_context(lang)
    context['authors'] = index['authors']
    context['header'] = context['loc_project_name']
    return context


def author_context(lang, author_id):
    context, index = _get_lang_context(lang)
    context['author'] = _get_author(index, author_id)
    context['header'] = context['author']['name']
    if author_id not in index['texts']:
        raise Http404('Requested text "{0}" is not found for author "{1}".'.format(text_id, author_id))

    context['texts'] = index['texts'][author_id]
    return context

def text_context(lang, author_id, text_id):
    context, index = _get_lang_context(lang)
    context['author'] = _get_author(index, author_id)
    context['text'] = _get_text(index, author_id, text_id)
    context['header'] = context['text']['name']
    return context