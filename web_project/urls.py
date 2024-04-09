# web_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Include URLs from the portfolio app
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)