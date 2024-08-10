from django.contrib import admin
from django.urls import path, include
from analyzer.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('analyzer.urls')),
    path('', index),  # This handles the root URL
]
