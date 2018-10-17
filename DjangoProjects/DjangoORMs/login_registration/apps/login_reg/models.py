from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def register_basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['firstname'] = "First name should be at least more than 2 characters"
        if len(postData['last_name']) < 1:
            errors['lastname'] = "Last name should be at least more than 2 characters"
        if postData['first_name'].isalpha()==False:
        	errors['firstname'] = "First Name must not contain any numbers"
        if postData['last_name'].isalpha()==False:
        	errors['firstname'] = "First Name must not contain any numbers"
        if len(postData['email']) < 8 and not EMAIL_REGEX.match(postData['email']):
        	errors['email']="Please fill email field!"
        if len(postData['password'])<8 or re.search('[0-9]', postData['password']) is None or re.search('[A-Z]', postData['password']) is None:
        	errors['password'] = "Password must be atleast 8 characters long, should contain one digit and one alphanumeric"
        if postData['password'] != postData['confirm_password']:
        	errors['password'] = "Passwords do not match",'confirm_password'
        if (self.filter(email=postData['email'])):
        	errors['email'] = "Email id already exists"
        return errors

    def login_basic_validator(self, postData):
    	errors = {}    	    	
    	if len(postData['login_email']) < 1:
    		errors['login_email'] = "Cannot login"
    	else:
    		users = self.filter(email=postData['login_email']) 
    		if len(users) < 1:
    			errors['login_email'] = "Email doesnot exist"
    	users = self.filter(email=postData['login_email'])
    	if len(postData['login_password']) < 1:
    		errors['login_password'] = "Password is required"
    	if users:
    		if not bcrypt.checkpw(postData['login_password'].encode(), users[0].password.encode()):
    			errors['login_password'] = "Password doesnot exist"
    	return errors    	



class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email, self.password)
		
	objects = UserManager()	