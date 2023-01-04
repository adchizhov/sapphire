from django.contrib.gis import forms
from django.conf import settings
from points.models import Point


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ('title', 'description', 'category', 'geom',)
        widgets = {
            'geom': forms.OSMWidget(
                attrs={
                    'map_width': 'auto',
                    'map_height': 500,
                    'default_zoom': settings.OSM_WIDGET_DEFAULT_ZOOM,
                    'default_lon': settings.OSM_WIDGET_DEFAULT_LON,
                    'default_lat': settings.OSM_WIDGET_DEFAULT_LAT
                }
            )
        }

