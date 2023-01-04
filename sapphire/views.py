from django.shortcuts import render


def custom_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def custom_error_view(request, *args, **kwargs):
    return render(request, '500.html', status=500)