from rest_framework import serializers
from .models import ProductoAPI

class ProductoAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductoAPI
        fields = '__all__'
        read_only_fields = ('created_at',)