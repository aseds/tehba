import datetime
from django.db import models
from django.utils import timezone 
# Create your models here
# if is_reliable == True, the admin-user himself should make 
# 'on' to be False
class Event(models.Model):
	SMALL_SIZE  = 1
	HALF_SIZE   = 2
	WIDE_SIZE   = 3
	SQUARE_SIZE = 4

	sizes = (
 		(SMALL_SIZE, 'small'),
 		(HALF_SIZE, 'half'),
 		(WIDE_SIZE, 'wide'),
 		(SQUARE_SIZE, 'square'),
	)

	name             = models.CharField(max_length=60)
	description      = models.TextField(max_length=550)
	size             = models.IntegerField(max_length=6, choices=sizes, default=SQUARE_SIZE)
	image            = models.ImageField(upload_to='images/', max_length=1000, null=True, blank=True)

	order            = models.IntegerField(default=-10)
	expired          = models.BooleanField(default=False)
	on               = models.BooleanField(default=False)

	expiration_date = models.DateTimeField('expires on')
	publish_date     = models.DateTimeField('date published', default=datetime.datetime.now() )


	def __unicode__(self):
		return self.name 

	def is_reliable(self):
		return self.expiration_date > timezone.now()
	is_reliable.boolean = True
	is_reliable.short_description = 'still active?'

#todo:
#
