from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import falkonconnectViewSet

router = DefaultRouter()
router.register("falkonconnect", falkonconnectViewSet, basename="falkonconnect")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
