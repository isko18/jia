from rest_framework import viewsets
from .models import Exhibition, Slider
from .serializers import ExhibitionSerializer, SliderSerializer

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
