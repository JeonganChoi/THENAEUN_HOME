from django.urls import path, re_path
from apps.views.home import indexViews

urlpatterns = [
    path('', indexViews.IndexViews, name="index"),
]