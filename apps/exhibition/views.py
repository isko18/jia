from rest_framework import viewsets
from .models import Exhibition, Slider, RentStand
from .serializers import ExhibitionSerializer, SliderSerializer, RentStandSerializer

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
class RentStandViewSet(viewsets.ModelViewSet):
    queryset = RentStand.objects.all()
    serializer_class = RentStandSerializer
