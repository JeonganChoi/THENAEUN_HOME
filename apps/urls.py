from django.urls import path, re_path
from apps.views.home import indexViews, serviceViews

urlpatterns = [
    path('', indexViews.IndexViews, name="index"),

    path('service', serviceViews.ServiceViews, name="service"),
]