from .models import ProductoAPI
from rest_framework import viewsets, permissions
from .serializers import ProductoAPISerializers

class ProductoAPIViewset(viewsets.ModelViewSet):
    queryset = ProductoAPI.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductoAPISerializers