from __future__ import unicode_literals

from django.db import models

# Create your models here.
	
class User(models.Model):
	name = models.TextField()
	
	class Meta:
		"""This is the table name in Database."""
		db_table = 'User'

class Question(models.Model):
	Title = models.TextField()
	private = models.BooleanField()
	user = models.ForeignKey(User)

	class Meta:
		"""This is the table name in Database."""
		db_table = 'Question'

class Answer(models.Model):
	body = models.TextField()
	question = models.ForeignKey(Question)
	user = models.ForeignKey(User)
	
	class Meta:
		"""This is the table name in Database."""
		db_table = 'Answer'
	
class Tenant(models.Model):
	name = models.TextField()
	api_key = models.TextField()
	api_request_count = models.IntegerField()
	
	class Meta:
		"""This is the table name in Database."""
		db_table = 'Tenant'
	
class ApiRequestCount(models.Model):
	date = models.DateTimeField()
	tenant = models.ForeignKey(Tenant)
	api_request = models.CharField(max_length=100)
	
	class Meta:
		"""This is the table name in Database."""
		db_table = 'ApiRequestCount'
