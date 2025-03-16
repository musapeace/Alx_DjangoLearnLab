from django.urls import path
from .views import AuthorListCreateView, BookListCreateView
from .views import BookListCreateView, BookDetailUpdateDeleteView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailUpdateDeleteView.as_view(), name="book-detail-update-delete"),
]
