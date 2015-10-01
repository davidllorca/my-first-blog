from django.db import models
from django.utils import timezone

# Models

class Post(models.Model): # models.Model -> Django model
	author = models.ForeignKey('auth.User') # Link with other model
	title = models.CharField(max_length=200) # text with length limit 
	text = models.TextField() # text with no limit
	created_date = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
