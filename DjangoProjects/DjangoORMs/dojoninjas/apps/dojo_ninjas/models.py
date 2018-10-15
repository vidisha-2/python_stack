from django.db import models

class Dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<Dojo object: {} {} {}>".format(self.name, self.city, self.state)

class Ninjas(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(Dojos, related_name="ninjas")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<Ninja object: {} {} {}>".format(self.first_name, self.last_name, self.dojo)