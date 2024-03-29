from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "bitcoin"

urlpatterns = [
    path('', views.bitcoin_view, name="bitcoin-view")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
