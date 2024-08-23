from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancingViewSet, ImageViewSet,  ReachViewSet, SectorViewSet, LegalNameViewSet, ImageViewSet, ExcelView, ImageFormViewSet

router = DefaultRouter()
router.register(r'financing', FinancingViewSet)
router.register(r'imageform', ImageViewSet)
router.register(r'nameinfo', ImageFormViewSet)
router.register(r'image', ImageViewSet)
router.register(r'reach', ReachViewSet)
router.register(r'sectors', SectorViewSet)
router.register(r'legal-names', LegalNameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view-excel/', ExcelView.as_view(), name='view-excel'),
]
