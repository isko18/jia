from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExhibitionViewSet, SliderViewSet

router = DefaultRouter()
router.register(r'exhibitions', ExhibitionViewSet)
router.register(r'sliders', SliderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
