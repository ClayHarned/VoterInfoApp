# django_pages/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    # path('', include('VoterInfo.urls')),
    # path('api/v1/', include('api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
