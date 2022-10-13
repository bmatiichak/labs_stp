from urllib.parse import urlparse
from django.urls import path
from app_blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view())
]