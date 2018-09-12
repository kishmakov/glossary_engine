from server.contexts import author_context, language_context, index_context, text_context

from django.http import HttpResponse
from django.template import Context, Template, loader

import markdown

import os


def language_view(request):
    t = loader.get_template('language.html')
    return HttpResponse(t.render(language_context(), request))


def index_view(request, lang):
    t = loader.get_template('index.html')
    return HttpResponse(t.render(index_context(lang), request))


def author_view(request, lang, author_id):
    t = loader.get_template('author.html')
    return HttpResponse(t.render(author_context(lang, author_id), request))


def text_view(request, lang, author_id, text_id):
    t = loader.get_template('text.html')
    return HttpResponse(t.render(text_context(lang, author_id, text_id), request))


def read_view(request, lang, author_id, text_id, part_id):
    author_dir = author_id.replace('_', ' ')
    file_name = part_id + '.md'
    full_name = os.path.join(os.path.dirname(__file__), '../gt', author_id[0], author_dir, file_name)

    md_file = open(full_name, 'r')
    html_text = markdown.markdown( md_file.read() )
    html_text = html_text.replace('<p>', '<p class="redfirst">')
    prefix = '{% extends "read.html" %} {% block text %}'
    suffix = '{% endblock %}'
    t = Template(prefix + html_text + suffix)
    return HttpResponse(t.render(Context(text_context(lang, author_id, text_id))))
