from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<lang>[a-z]{2})/', views.index_view),
    path('', RedirectView.as_view(url='ru/', permanent=True))
]

