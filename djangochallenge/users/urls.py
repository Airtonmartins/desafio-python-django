from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('me', views.user_info),
]