from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^testing/$', views.test, name='test'),
	url(r'^profile/$', views.profile, name='profile'),
)