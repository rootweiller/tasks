from __future__ import unicode_literals

from django.db import models



class EnglishLevel(models.Model):

	field_name = models.CharField(max_length=75)


	def __unicode__(self):

		return self.field_name


class Country(models.Model):

	field_name = models.CharField(max_length=75)


	def __unicode__(self):

		return self.field_name


class Candidate(models.Model):

	name = models.CharField(max_length=75, unique=True)
	job_position = models.CharField(max_length=75)
	email = models.EmailField()
	hours_per_week = models.IntegerField()
	where_found_us = models.CharField(max_length=75)
	country = models.ForeignKey(Country)
	english_level = models.ForeignKey(EnglishLevel)
	comments = models.CharField(max_length=150, blank=True)



	def __unicode__(self):

		return self.name




