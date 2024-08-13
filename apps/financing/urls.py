from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancingViewSet,ImageViewSet,  ReachViewSet, SectorViewSet, LegalNameViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'financing', FinancingViewSet)
router.register(r'nameinfo', ImageViewSet)
# router.register(r'imageform', ImageFormViewSet)
router.register(r'image', ImageViewSet)
router.register(r'reach', ReachViewSet)
router.register(r'sectors', SectorViewSet)
router.register(r'legal-names', LegalNameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
