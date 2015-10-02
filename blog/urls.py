from django.conf.urls import include, url
from . import views # Import all views of 'blog'

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail), 

]

