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
    family = OsFamilySerializer()
    class Meta:
        model = OperatingSystem


class InstanceSerializer(serializers.ModelSerializer):
    operating_system = OperatingSystemSerializer(many=True)

    class Meta:
        model = Instance


class ServerPlanSerializer(serializers.ModelSerializer):
    instance = InstanceSerializer()
    provider = ProviderSerializer()
    class Meta:
        model = ServerPlan
