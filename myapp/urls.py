from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"

urlpatterns = [
    path('', views.ProductList.as_view(), name="products"),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name="product-detail"),
    path('product-update/<int:pk>/', views.ProductUpdate.as_view(), name="product-update")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
