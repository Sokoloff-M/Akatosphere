from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from products import views as product_views

# Инициализация роутера API
router = DefaultRouter()
router.register(r'categories', product_views.CategoryViewSet, basename='categories')
router.register(r'products', product_views.ProductViewSet, basename='products')

urlpatterns = [
    # Перенаправление корневого URL на документацию
    path('', RedirectView.as_view(url='/api/docs/', permanent=True)),
    
    # Административная панель
    path('admin/', admin.site.urls),
    
    # API Endpoints
    path('api/', include([
        path('', include(router.urls)),
        
        # Аутентификация
        path('auth/', include([
            path('', include('rest_framework.urls')),  # DRF Session Auth
            path('token/', include('djoser.urls.authtoken')),  # Token Auth
        ])),
        
        # Документация
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ])),
    
    path('health/', include('health_check.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)