from django.contrib import admin
from django.urls import path, include

from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
]