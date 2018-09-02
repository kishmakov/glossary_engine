from server.contexts import index_context
from server.settings import BASE_DIR

from django.http import HttpResponse, Http404
from django.template import loader


import json
import os


def index_view(request, lang):
    index_file = os.path.join(BASE_DIR, 'index_{0}.json'.format(lang))
    if not os.path.isfile(index_file):
        raise Http404('Requested lang "{0}" is not supported.'.format(lang))

    t = loader.get_template('base.html')
    with open(index_file) as input:
        index = json.load(input)

    return HttpResponse(t.render(index_context(lang, index), request))

