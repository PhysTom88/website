from django.db import models
from django.utils import timezone


class TextDescription(models.Model):
	'''Model for large pieces of text'''

	block_name = models.CharField(max_length=250, unique=True)
	block_text = models.TextField('Text')
	mod_date = models.DateField(blank=True, null=True)
	text_location = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.block_name


class BlogPost(models.Model):
	'''Model for blog posts'''
	SUBJECT_CHOICE = (
		('TEST', 'Test'),
		)

	title = models.CharField(max_length=250, unique=True)
	text = models.TextField('blog text')
	subject = models.CharField(max_length=250, choices=SUBJECT_CHOICE, blank=True, null=True)
	created_date = models.DateField(default=timezone.now)
	published_date = models.DateField(blank=True, null=True)
	post_image = models.ImageField(upload_to='blog/images/', max_length=100,
								   blank=True, null=True)

	slug = models.SlugField(max_length=255, default=None, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title
