from django.conf.urls import url

from website.views import main

urlpatterns = [
	url(r'^$', main.home, name='main'),
	url(r'^about/$', main.about, name='about'),
]