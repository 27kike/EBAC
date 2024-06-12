from django.db import models

# Create your models here.
class ProductoAPI(models.Model):
    title = models.CharField(max_length=200, verbose_name='Nombre del Producto')
    category = models.CharField(max_length=200, verbose_name='Categoría')
    contry = models.CharField(max_length=10, verbose_name='País')
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("create_at",)