from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

from sites.models import Site


class PointCategory(models.Model):
    name = models.CharField('site name', max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
        ]

    def __str__(self):
        return self.name


class Point(models.Model):
    """
    it could be category 'hazard' or any other, that's why it is not called Hazard and has FK to PointCategory
    """
    title = models.CharField('point title', max_length=100)
    description = models.CharField('point description', max_length=256)
    geom = models.PointField(srid=settings.DEFAULT_SRID)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(PointCategory, related_name='points', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='points_title_idx'),
        ]

    def __str__(self):
        return f'{self.title} with id: {self.pk}'

    @property
    def popup_info(self):
        """
        Formatted text for use on the map
        :return:
        """
        return f'<p>category: {self.category}</p>' \
               f'<p>title: {self.title}</p>' \
               f'<p>description: {self.description}</p>' \
               f'<p><a href={self.get_absolute_url()}>view</a></p>'

    @property
    def found_in_sites(self):
        """
        list of sites that contains the point
        :return:
        """
        return Site.objects.filter(polygon__intersects=self.geom)

    def get_absolute_url(self):
        return reverse('points:detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('points:edit', kwargs={'pk': self.pk})
