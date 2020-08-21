from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickstart/', include('quickstart.urls')),
    path('modelformapp/', include('modelformapp.urls')),
    path('company/', include('company.urls')),
]
