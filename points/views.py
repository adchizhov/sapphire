from django.urls import reverse_lazy

from points.forms import PointForm
from django.views import generic

from points.models import Point


class PointCreateView(generic.CreateView):
    template_name = 'points/create_or_edit.html'
    form_class = PointForm
    model = Point

    def get_success_url(self):
        return reverse_lazy('points:detail', kwargs={'pk': self.object.pk})


class PointEditView(generic.UpdateView):
    template_name = 'points/create_or_edit.html'
    form_class = PointForm
    model = Point

    def get_success_url(self):
        return reverse_lazy('points:detail', kwargs={'pk': self.object.pk})


class PointDetailView(generic.DetailView):
    model = Point
    template_name = 'points/detail.html'
