from django.shortcuts import render
from rest_framework import generics


from .serializers import CandidateSerializers
from .models import Candidate
from rest_framework.response import Response




class CandidateView(generics.ListAPIView):

	queryset = Candidate.objects.all()

	serializer_class = CandidateSerializers



class CandidateCreate(generics.CreateAPIView):

	queryset = Candidate.objects.all()

	serializer_class = CandidateSerializers


class CandidateRetrive(generics.RetrieveAPIView):

	queryset = Candidate.objects.all()

	serializer_class = CandidateSerializers


class CandidateUpdate(generics.UpdateAPIView):

	queryset = Candidate.objects.all()

	serializer_class = CandidateSerializers