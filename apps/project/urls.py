from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, YearlyCatalogViewSet, ScrollViewSet, BusinessProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'yearly-catalogs', YearlyCatalogViewSet)
router.register(r'scrolls', ScrollViewSet)
router.register(r'business-projects', BusinessProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
