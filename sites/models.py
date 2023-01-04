from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse


class Site(models.Model):
    title = models.CharField('title', max_length=100)
    polygon = models.PolygonField('polygon', srid=settings.DEFAULT_SRID)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='sites_title_idx'),
        ]

    def __str__(self):
        return f'{self.title} with id: {self.pk}'

    @property
    def points_within_site(self):
        """
        Get all points within site
        :return:
        """
        from points.models import Point  # deals with cross import
        return Point.objects.filter(geom__within=self.polygon)

    def get_absolute_url(self):
        return reverse('sites:detail', kwargs={'pk': self.pk})