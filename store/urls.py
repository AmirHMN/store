from django.urls import path, include
from . import views
from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customer', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, 'product-review')
cart_router = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-item')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls))
]
