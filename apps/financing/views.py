from rest_framework import viewsets
from .models import Financing, Image, Reach, Sector, LegalName, NameInfo, ImageForm
from apps.financing.serializers import FinancingSerializer, ImageSerializer, ReachSerializer, SectorSerializer, LegalNameSerializer, ImageFormSerializer

class FinancingViewSet(viewsets.ModelViewSet):
    queryset = Financing.objects.all()
    serializer_class = FinancingSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImageForm.objects.all()
    serializer_class = ImageFormSerializer

    
class ReachViewSet(viewsets.ModelViewSet):
    queryset = Reach.objects.all()
    serializer_class = ReachSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class LegalNameViewSet(viewsets.ModelViewSet):
    queryset = LegalName.objects.all()
    serializer_class = LegalNameSerializer
