from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'category',
        ]

    # def validate_price(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Price must be greater than zero.")
    #     return value
