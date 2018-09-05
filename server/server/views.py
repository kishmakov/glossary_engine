from server.contexts import author_context, language_context, index_context, text_context

from django.http import HttpResponse
from django.template import loader


def language_view(request):
    t = loader.get_template('language.html')
    return HttpResponse(t.render(language_context(), request))


def index_view(request, lang):
    t = loader.get_template('welcome.html')
    return HttpResponse(t.render(index_context(lang), request))


def author_view(request, lang, author_id):
    t = loader.get_template('author.html')
    return HttpResponse(t.render(author_context(lang, author_id), request))

def text_view(request, lang, author_id, text_id):
    t = loader.get_template('text.html')
    return HttpResponse(t.render(text_context(lang, author_id, text_id), request))


