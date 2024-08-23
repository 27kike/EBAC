from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre del producto')
    type = models.CharField(max_length=20, verbose_name='Tipo de producto')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Precio' )
    class Meta:
        ordering = ['name','type']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'