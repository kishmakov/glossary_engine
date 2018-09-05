from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.language_view),
    re_path(r'^(?P<lang>[a-z]{2})/$', views.index_view),
    re_path(r'^(?P<lang>[a-z]{2})/(?P<author_id>[\w_]+)/$', views.author_view),
    re_path(r'^(?P<lang>[a-z]{2})/(?P<author_id>[\w_]+)/(?P<text_id>[\w_]+)/$', views.text_view),
]

