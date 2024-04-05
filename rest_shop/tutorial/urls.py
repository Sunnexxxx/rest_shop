from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('shop.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('auth_users.urls')),
    path('api/v1/', include('shop.api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
