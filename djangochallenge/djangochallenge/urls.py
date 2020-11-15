
from django.contrib import admin
from django.urls import include, path

from users.views import obtain_jwt_token

urlpatterns = [
    path('api/signin', obtain_jwt_token),
    path('api/', include('users.urls')),
]
