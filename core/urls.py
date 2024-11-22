from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksBookViewSet

router = DefaultRouter()
router.register(r'books', BooksBookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
