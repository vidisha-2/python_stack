from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)


class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
	users_who_like = models.ManyToManyField(User, related_name="liked_books")

	def __repr__(self):
		return "<User object: {} {}>".format(self.name, self.desc)

