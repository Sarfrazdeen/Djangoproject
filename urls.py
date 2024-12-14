from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin page
    path('', include('backend.urls')),  # Root URL routed to 'backend' app
    path('auth/',include('Authentication.urls'))
]

# Serve static files during development when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
