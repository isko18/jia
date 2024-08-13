from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutMixins, AboutBannerMixins, HistoryMixins, HistoryDetailMixins, StatisticsMixins, GalleryMixins

router = DefaultRouter()

(
router.register(r'about', AboutMixins, basename='about'),
router.register(r'about_banner', AboutBannerMixins, basename='about_banner'),
router.register(r'history', HistoryMixins, basename='history'),
router.register(r'history_detail', HistoryDetailMixins, basename='history_detail'),
router.register(r'statistics', StatisticsMixins, basename='statistics'),
router.register(r'gallery', GalleryMixins, basename='gallery'),
)

urlpatterns = router.urls