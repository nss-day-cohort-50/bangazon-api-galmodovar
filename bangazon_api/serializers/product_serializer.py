from rest_framework import serializers
from bangazon_api.models import Product
class ProductSerializer(serializers.ModelSerializer):
    order_count = serializers.IntegerField(default=None)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'average_rating', 'quantity', 'location', 'image_path', 'category', 'store', 'order_count')
        depth = 1

class CreateProductSerializer(serializers.Serializer):
    categoryId = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=7)
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    location = serializers.CharField()
    image = serializers.ImageField()

class AddRemoveRecommendationSerializer(serializers.Serializer):
    username = serializers.CharField()

class AddProductRatingSerializer(serializers.Serializer):
    score = serializers.IntegerField()
