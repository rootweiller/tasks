from rest_framework import serializers
from .models import Candidate, EnglishLevel, Country



class CandidateSerializers(serializers.ModelSerializer):


	class Meta:

		model = Candidate

		fields = '__all__'



class EnglishLevelSerializer(serializers.ModelSerializer):


	class Meta:

		model = EnglishLevel


		fields = ['field_name']



class CountrySerializer(serializers.ModelSerializer):


	class Meta:

		model = Country


		fields = ['country']