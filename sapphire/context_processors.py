from django.conf import settings

from sites.views import SiteSearchListView


def project_name(request):
    return {'project_name': settings.PROJECT_NAME}


def current_search_value(request):
    """
    Get title_q from request if presented
    :param request:
    :return:
    """
    search_key = SiteSearchListView.search_field
    current_search_value = f'&{search_key}={request.GET.get(search_key)}' if request.GET.get(search_key) else ''
    return {'current_search_value': current_search_value}