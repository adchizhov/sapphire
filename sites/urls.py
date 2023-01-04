from django.urls import path
from sites.views import SiteListView, SiteSearchListView, SiteDetailView

urlpatterns = [
    path("", SiteListView.as_view(), name="list"),
    path("search", SiteSearchListView.as_view(), name="search"),
    path("<int:pk>", SiteDetailView.as_view(), name="detail"),
]
