from django.contrib import admin

from .models import (
    Provider,
    OsFamily,
    OperatingSystem,
    Instance,
    ServerPlan)


admin.site.register(Provider)
admin.site.register(OsFamily)
admin.site.register(OperatingSystem)
admin.site.register(Instance)
admin.site.register(ServerPlan)
