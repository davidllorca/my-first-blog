from django.conf.urls import include, url
from . import views # Import all views of 'blog'

urlpatterns = [
	url(r'^$', views.post_list),
]
