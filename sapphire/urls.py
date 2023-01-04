from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("", lambda request: redirect("sites:list")),
    path("sites/", include(("sites.urls", "sites"),
                           namespace="sites")),
    path("points/", include(("points.urls", "points"),
                            namespace="points")),
]
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)

handler404 = 'sapphire.views.custom_not_found_view'
handler500 = 'sapphire.views.custom_error_view'
