from server.contexts import index_context, author_context
from server.settings import BASE_DIR

from django.http import HttpResponse, Http404
from django.template import loader

import json
import os


def get_index(lang):
    index_file = os.path.join(BASE_DIR, 'index_{0}.json'.format(lang))
    if not os.path.isfile(index_file):
        raise Http404('Requested lang "{0}" is not supported.'.format(lang))

    with open(index_file) as input:
        return json.load(input)


def index_view(request, lang):
    index = get_index(lang)
    t = loader.get_template('welcome.html')

    return HttpResponse(t.render(index_context(lang, index), request))


def author_view(request, lang, author_id):
    index = get_index(lang)
    t = loader.get_template('author.html')

    return HttpResponse(t.render(author_context(lang, index, author_id), request))


