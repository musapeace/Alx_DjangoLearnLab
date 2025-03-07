from django.urls import path, include
from .views import BookList
from .views import BookViewSet
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Book list API endpoint
    path('', include(router.urls)),
    path('list/', BookList.as_view(), name='book-list'),
]
