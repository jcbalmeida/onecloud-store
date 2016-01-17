from rest_framework import serializers
from .models import (
    Provider,
    OsFamily,
    OperatingSystem,
    Instance,
    ServerPlan
)


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider


class OsFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = OsFamily


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance


class ServerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerPlan
