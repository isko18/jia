from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationViewSet,
    StandartViewSet,
    VipViewSet,
    SectorStandartViewSet,
    ReachStandartViewSet,
    SectorVipViewSet,
    ReachVipViewSet
)

# Создаем роутер и регистрируем наши ViewSet
router = DefaultRouter()
router.register(r'registration', RegistrationViewSet)
router.register(r'standart', StandartViewSet)
router.register(r'vip', VipViewSet)
router.register(r'sector-standart', SectorStandartViewSet)
router.register(r'reach-standart', ReachStandartViewSet)
router.register(r'sector_vip', SectorVipViewSet)
router.register(r'reach_vip', ReachVipViewSet)

# Подключаем маршруты, созданные роутером, в urls.py
urlpatterns = [
    path('', include(router.urls)),  # Маршруты для API будут доступны по /api/
]
