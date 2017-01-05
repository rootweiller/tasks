from django.conf.urls import *
from django.contrib import admin

from .views import *
from .config import *

urlpatterns = [
    url(r'^api/v1/candidate/list', CandidateView.as_view(), name='CandidateList'),
    url(r'^api/v1/candidate/(?P<pk>[\d]+)/$', CandidateView.as_view(), name='CandidateDetail'),

    #Create
    url(r'api/v1/candidate/add/$', CandidateCreate.as_view(), name='CandidateCreate'),

    #Update
    url(r'api/v1/candidate/update/(?P<pk>[0-9]+)', CandidateUpdate.as_view(), name='CandidateUpdate'),


    #Config
    url(r'api/v1/dropdowns/add', EnglishLevelAdd.as_view(), name='EnglishLevelAdd'),
    url(r'api/v1/dropdowns', EnglishLevelDetail.as_view(), name='EnglishLevelAll'),
    url(r'api/v1/dropdowns/(?P<slug>[-\w]+)/$', EnglishLevelDetail.as_view(), name='EnglishLevelDetail'),
]
