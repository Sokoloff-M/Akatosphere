from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from .models import Category, Product  # Убедитесь, что модели существуют в models.py
from .serializers import CategorySerializer, ProductSerializer

def home(request):
    """Главная страница API"""
    return HttpResponse("""
        <h1>Добро пожаловать в Food Market API</h1>
        <a href="/api/docs/">Swagger UI</a><br>
        <a href="/admin/">Админка</a>
    """)

class StandardResultsSetPagination(PageNumberPagination):
    """Кастомная пагинация"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для категорий товаров"""
    queryset = Category.objects.prefetch_related('subcategories').all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug'  # Для работы с slug вместо id

class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet для товаров"""
    queryset = Product.objects.select_related('subcategory__category').all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug'
    filterset_fields = ['subcategory__category__slug', 'subcategory__slug']  # Фильтрация