from rest_framework import routers
from .views import ProductoViewset

router = routers.DefaultRouter()
router.register('productos-hellb',ProductoViewset,'productos/hellb')

urlpatterns = router.urls