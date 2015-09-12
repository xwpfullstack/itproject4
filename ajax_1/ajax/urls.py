from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itcast_project4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', views.index),
    url(r'^add/', views.add),
)

