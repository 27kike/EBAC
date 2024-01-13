import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
articulos = {
    'Camisa':200,
    'Gorra':120,
    'Monitor':5000,
    'Xbox':3500,
    'Celular':1200,
    'Laptop':9000
}
articulosDisponibles = {
    'Mouse':90,
    'Ipad':1200,
    'Cargador':67,
    'Cable USB':10,
    'Tenis':600,
    'Mochila':230
}
class Utilidades:
    articulo = ''
    def __init__(self,articulos = '',articulosDisp = ''):
        self.articulos = articulos
        self.articulosDisp = articulosDisp
        
    def mostrarArticulos(self,carrito = 1):
        if carrito:
            print('Mostrando los articulos de tu carrito\n\n')
            for indice, articulo in enumerate(self.articulos,start = 1):
                print('{}).- {}'.format(indice,articulo))
        else:
            print('Mostrando los articulos disponibles\n\n')
            for indice, articulo in enumerate(self.articulosDisp,start = 1):
                print('{}).- {}'.format(indice,articulo))

    def quitarArticulo(self):
        articulo = input('¿Que articulo quieres eliminar?: ')
        try:
            del articulos[articulo]
        except KeyError as e:
            print('El articulo {} no existe en tu carrito.'.format(e))
        else:
            print('El articulo {} se elimino correctamente.'.format(articulo))

    def agregarArticulo(self):
        self.mostrarArticulos(0)
        self.mostrarArticulos(1)
        articulo = input('¿Que articulo quieres agregar?')
        try:
            self.articulos[articulo] = self.articulosDisp[articulo]
        except KeyError as e:
            print('Error al agregar el articulo: {}.'.format(e))
        else:
            print('El articulo: {} se agrego correctamente.'.format(articulo))

class Carrito(Utilidades):
    totalPago = 0
    def __init__(self,articulos = '',articulosDisp = ''):
        super().__init__(articulos,articulosDisp)

    def total(self):
        totalPago = sum(precio for precio in self.articulos.values())
        return 'El pago total es: {} pesos'.format(totalPago)

def home(request):
    carrito = Carrito(articulos,articulosDisponibles)
    pago = carrito.total()
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + " PROBANDO",
        "python_ver": os.environ["PYTHON_VERSION"] + ' MAS CAMBIOS',
        "pago":pago,
    }

    return render(request, "pages/home.html", context)