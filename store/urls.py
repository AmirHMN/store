from django.urls import path
from .views import CollectionList, collection_detail, ProductList, ProductDetail, CollectionDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('collections/', CollectionList.as_view()),
    path('collections/<int:pk>', CollectionDetail.as_view())
]
