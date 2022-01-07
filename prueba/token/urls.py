"""Experience URLs."""

# Django
from django.urls import include, re_path    
# Django REST Framework
from rest_framework.routers import DefaultRouter
# Views
from token import view

router = DefaultRouter()
router.register(r'token', view.TokenViewSet, basename='token')

urlpatterns = [
    re_path('', include(router.urls))
]