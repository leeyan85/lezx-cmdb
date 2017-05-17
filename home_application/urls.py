# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^get_app_list/$', 'get_app_list'),
    (r'^get_city_list/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
)
