from django.conf.urls import url
from . import views

app_name = "ACMS"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.index, name='login_index'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^workpage/$', views.workpage, name='workpage')


]
