from django.db import models
from apps.login_reg.models import *


class MessageManager(models.Manager):
    def my_validator(self, postData):
        errors = {}
        if len(postData["message"]) < 2:
            errors["message"] = "Empty"
        return errors


class Message(models.Model):
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="messages")
	objects = MessageManager() 
	def __str__(self):
		return f'{self.message}'

class Comment(models.Model):
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message = models.ForeignKey(Message, related_name="comments")
	user = models.ForeignKey(User, related_name="comments")
	# objects = MessageManager()
	def __str__(self):
		return f'{self.comment}'	
