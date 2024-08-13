from rest_framework import viewsets
from .models import Project, YearlyCatalog, Scroll, BusinessProject
from .serializers import ProjectSerializer, YearlyCatalogSerializer, ScrollSerializer, BusinessProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class YearlyCatalogViewSet(viewsets.ModelViewSet):
    queryset = YearlyCatalog.objects.all()
    serializer_class = YearlyCatalogSerializer

class ScrollViewSet(viewsets.ModelViewSet):
    queryset = Scroll.objects.all()
    serializer_class = ScrollSerializer

class BusinessProjectViewSet(viewsets.ModelViewSet):
    queryset = BusinessProject.objects.all()
    serializer_class = BusinessProjectSerializer
