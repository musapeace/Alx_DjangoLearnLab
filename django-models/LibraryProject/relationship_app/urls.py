from django.urls import path
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, user_register
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
<<<<<<< HEAD
    path("register/", views.register, name="register"),
=======
    path("register/", views.user_register, name="register"),
>>>>>>> 28373a65148e553d7d23e34bea1ec200a0aa1f67
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
