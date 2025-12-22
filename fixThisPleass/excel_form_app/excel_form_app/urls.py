from django.contrib import admin
from django.urls import path, include  # make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # include your app URLs
]
