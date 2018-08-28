from django.http import HttpResponse
from django.template import loader

from server.contexts import index_context

def index_view(request, lang):
	t = loader.get_template('base.html')
	return HttpResponse(t.render(index_context(lang), request))

