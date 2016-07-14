from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.first_page, name='first_page'),
     url(r'^post/(?P<pk>\d+)/$', views.second_page, name='second_page'),
      url(r'^post/new/$', views.post_new, name='post_new'),
      url(r'^post/(?P<pk>\d+)/edit/$', views.page_edit, name='page_edit'),
]
