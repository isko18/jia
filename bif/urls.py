from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns_swagger
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.base.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += urlpatterns_swagger

urlpatterns += i18n_patterns(
    path('api/v1/base/', include('apps.base.urls')),
    path('api/v1/about/', include('apps.about.urls')),
    path('api/v1/financing/', include('apps.financing.urls')),
    path('api/v1/project/', include('apps.project.urls')),  
    path('api/v1/exhibition/', include('apps.exhibition.urls')),
    path('api/v1/registration/', include('apps.registration.urls')),
    
    
    path('', index, name='index'),  # Главная страница для всех языков
    path('<path:path>', index),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
