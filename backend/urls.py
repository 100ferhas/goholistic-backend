from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('', include('bookings.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
