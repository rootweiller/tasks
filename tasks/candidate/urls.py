from django.conf.urls import *
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^candidate/list', CandidateView.as_view(), name='CandidateList'),
    url(r'^candidate/(?P<pk>[\d]+)/$', CandidateView.as_view(), name='CandidateDetail'),

    #Create
    url(r'candidate/add/$', CandidateCreate.as_view(), name='CandidateCreate'),

    #Update
    url(r'candidate/update/(?P<pk>[0-9]+)', CandidateUpdate.as_view(), name='CandidateUpdate'),
]
