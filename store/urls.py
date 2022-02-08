from django.urls import path, include
from . import views
from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
router.register('collections', views.CollectionViewSet)
product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, 'product-review')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
]
