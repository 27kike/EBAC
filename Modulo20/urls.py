from rest_framework import routers
from .api import ProductoAPIViewset

router = routers.DefaultRouter()
router.register('producto', ProductoAPIViewset, 'producto')
urlpatterns = router.urls