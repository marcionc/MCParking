"""mcparking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from estacionamento.api.viewsets import EstacionamentoViewSet
from veiculos.api.viewsets import VeiculosViewSet
from vagas.api.viewsets import VagasViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'estacionamento', EstacionamentoViewSet, basename='Estacionamento')
router.register(r'veiculos', VeiculosViewSet, basename='Veiculo')
router.register(r'vagas', VagasViewSet, basename='Vaga')

urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token)
]
