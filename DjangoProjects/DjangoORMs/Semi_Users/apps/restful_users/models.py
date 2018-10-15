from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name should be at least more than 1 characters"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name should be at least more than 1 characters"
        if len(postData['email']) < 10:
            errors['email'] = "Blog description should be at least 10 characters"
        return errors


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)
		
	objects = UserManager()	
