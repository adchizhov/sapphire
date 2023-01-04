from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

from points.models import Point


class Site(models.Model):
    title = models.CharField('title', max_length=100)
    polygon = models.PolygonField('polygon', srid=settings.DEFAULT_SRID)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='sites_title_idx'),
        ]

    def __str__(self):
        return f'Site: {self.title} with pk <{self.pk}>'

    @property
    def hazard_points(self):
        """
        Get Hazard points within site
        :return:
        """
        return Point.objects.filter(geom__within=self.polygon, category__name='Hazard')

    @property
    def shelter_points(self):
        """
        Get Shelter points within site
        :return:
        """
        return Point.objects.filter(geom__within=self.polygon, category__name='Shelter')

    @property
    def all_points_within(self):
        """
        Get all points within site
        :return:
        """
        return Point.objects.filter(geom__within=self.polygon)

    def get_absolute_url(self):
        return reverse('sites:detail', kwargs={'pk': self.pk})