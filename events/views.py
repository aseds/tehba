from django.shortcuts import render
from events.models import Event 

# Create your views here.
def list_events(request):
	latest_event_list = Event.objects.filter(on=True)[:10]
	context = {'today_events': latest_event_list}
	return render(request, 'events/index.html', context)