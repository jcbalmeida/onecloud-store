from rest_framework import viewsets
from .serializers import (
    ProviderSerializer,
    OsFamilySerializer,
    OperatingSystemSerializer,
    InstanceSerializer,
    ServerPlanSerializer
)
from .models import (
    Provider,
    OsFamily,
    OperatingSystem,
    Instance,
    ServerPlan
)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by("name")
    serializer_class = ProviderSerializer


class OsFamilyViewSet(viewsets.ModelViewSet):
    queryset = OsFamily.objects.all().order_by("name")
    serializer_class = OsFamilySerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all().order_by("name")
    serializer_class = OperatingSystemSerializer


class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


class ServerPlanViewSet(viewsets.ModelViewSet):
    queryset = ServerPlan.objects.all().order_by('price')
    serializer_class = ServerPlanSerializer
