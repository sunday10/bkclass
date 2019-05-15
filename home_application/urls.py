# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^helloworld/$', 'helloworld'),
    (r'^hellosunday/$', 'hellosunday'),
    (r'^test/$', 'test'),
)