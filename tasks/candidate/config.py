from django.shortcuts import render
from rest_framework import generics


from .serializers import EnglishLevelSerializer, CountrySerializer
from .models import EnglishLevel, Country
from rest_framework.response import Response






class EnglishLevelAdd(generics.CreateAPIView):

	queryset = EnglishLevel.objects.all()

	serializer_class = EnglishLevelSerializer



class CountrySerializer(generics.CreateAPIView):

	queryset = Country.objects.all()

	serializer_class = CountrySerializer



class EnglishLevelDetail(generics.ListAPIView):

	queryset = EnglishLevel.objects.all()


	serializer_class = EnglishLevelSerializer


