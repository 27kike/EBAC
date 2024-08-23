from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializers

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializers