from __future__ import unicode_literals

from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OsFamily(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    family = models.ForeignKey(OsFamily, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.name, self.version)


class Instance(models.Model):
    name = models.CharField(max_length=50)
    v_cpu = models.IntegerField()
    memory = models.FloatField()
    disk_space = models.FloatField()
    operating_system = models.ManyToManyField(OperatingSystem)

    def __str__(self):
        return self.name


class ServerPlan(models.Model):
    name = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} - {} ($ {}/h)".format(self.provider.name, self.name, self.price)
