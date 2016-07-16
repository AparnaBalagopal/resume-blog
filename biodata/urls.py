from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.first_page, name='first_page'),
	url(r'^post/(?P<pk>\d+)/$', views.second_page, name='second_page'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.page_edit, name='page_edit'),
	url(r'^niit/$', views.niit, name='niit'),
	url(r'^bca/$', views.bca, name='bca'),
	url(r'^hse/$', views.hse, name='hse'),
	url(r'^sslc/$', views.sslc, name='sslc'),

]
