from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from sites.models import Site


class SiteListView(generic.ListView):
    paginate_by = 10
    template_name = 'sites/list.html'
    context_object_name = 'all_sites'

    def get_queryset(self):
        return Site.objects.order_by('pk')


class SiteSearchListView(generic.ListView):
    paginate_by = 10
    template_name = 'sites/list.html'
    context_object_name = 'search_results'
    search_field = 'title_q'

    def get_queryset(self):
        title_q = self.request.GET.get(self.search_field)
        if not title_q:
            raise Http404('Empty search request provided')

        found_entities = Site.objects.filter(title__icontains=title_q)
        return found_entities


class SiteDetailView(generic.DetailView):
    model = Site
    template_name = 'sites/detail.html'