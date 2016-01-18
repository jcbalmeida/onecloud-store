"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from store.computing import api
from django.views.generic import TemplateView
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'providers', api.ProviderViewSet)
router.register('os-families', api.OsFamilyViewSet)
router.register('os', api.OperatingSystemViewSet)
router.register('instances', api.InstanceViewSet)
router.register('plans', api.ServerPlanViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(
        '^static/(?P<path>.*)',
        'django.views.static.serve',
        {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }
    ),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
