from django.urls import path

from points.views import PointCreateView, PointEditView, PointDetailView

urlpatterns = [
    path('detail/<int:pk>', PointDetailView.as_view(), name='detail'),
    path("create", PointCreateView.as_view(), name="create"),
    path("edit/<int:pk>", PointEditView.as_view(), name="edit"),
]