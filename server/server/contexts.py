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


def prepare_lang_context(lang):
    if not lang in localizations:
        raise Http404('Requested lang "{0}" is not supported.'.format(lang))

    context = localizations[lang]
    context['lang'] = lang
    return context, indexes[lang]


def language_context():
    langs = []
    for code, lc in sorted(localizations.items()):
        langs.append({'code': code, 'selfname': lc['loc_selfname'], 'flag': lc['loc_flag']})
    return {'langs': langs}


def index_context(lang):
    context, index = prepare_lang_context(lang)
    context['authors'] = index['authors']
    context['header'] = context['loc_project_name']
    return context


def author_context(lang, author_id):
    context, index = prepare_lang_context(lang)
    context['author_id'] = author_id
    context['author_name'] = index['author'][author_id]['name']
    context['header'] = context['author_name']
    context['texts'] = index['author'][author_id]['texts']
    return context