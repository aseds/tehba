from django.contrib import admin
from events.models import Event 

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'on', 'is_reliable', 'order')
	list_filter = ['order']
admin.site.register(Event, EventAdmin)