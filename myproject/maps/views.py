import json
from django.shortcuts import render
from .models import Waypoint

def map_view(request):
    waypoints = Waypoint.objects.all()
    waypoint_data = [
        {"name": wp.name, "lat": wp.latitude, "lng": wp.longitude}
        for wp in waypoints
    ]
    return render(request, 'map.html', {
        'waypoints_json': json.dumps(waypoint_data)
    })