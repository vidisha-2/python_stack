from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors={}
		if len(postData['name']) < 5:
			errors['name'] = "Course name should be at least more than 5 characters"
		# if len(postData['desc']) < 15:
		# 	errors['desc'] = "Description Field should be at least more than 15 characters"
		return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	date_added = models.DateTimeField(auto_now_add=True)
	# objects = CourseManager()

	def __str__(self):
		return f'{self.name}, {self.date_added}'


class Description(models.Model):
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	course = models.OneToOneField(Course, primary_key=True, related_name="description")

	def __str__(self):
		return f'{self.desc}'





