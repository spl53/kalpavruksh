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
	
	class Meta:
		"""This is the table name in Database."""
		db_table = 'Tenant'
