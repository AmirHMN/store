from rest_framework import serializers
from store.models import Collection, Product, Review


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()

    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']


class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'title',  'unit_price','collection']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
