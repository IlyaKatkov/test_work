from rest_framework.routers import DefaultRouter

from electronics_shop.apps import ElectronicsShopConfig
from electronics_shop.views import SupplierViewSet, ProductViewSet, ContactViewSet

app_name = ElectronicsShopConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls