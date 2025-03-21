from django.urls import path, include
from .views import BookList
from .views import BookViewSet
from rest_framework import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Book list API endpoint
    path('', include(router.urls)),
    path('list/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
