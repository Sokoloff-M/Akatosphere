from rest_framework import serializers
from .models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'image', 'category']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.StringRelatedField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'subcategory', 'price', 'images']

    def get_category(self, obj):
        return obj.subcategory.category.name

    def get_images(self, obj):
        return {
            'small': obj.image_small.url,
            'medium': obj.image_medium.url,
            'large': obj.image_large.url
        }