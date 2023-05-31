from django.urls import include, path
from rest_framework import routers
# from django.urls.conf import re_path
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'purchase', views.PurchaseViewSet)
router.register(r'master', views.AllMasterViewSet)


urlpatterns = [
    path('', include(router.urls)),    
]
