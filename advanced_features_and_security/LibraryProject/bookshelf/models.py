from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.DateField()

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

class CustomUserManager(BaseUserManager):
    """Custom manager for the CustomUser model."""

    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        """Creates and returns a regular user."""
        if not email:
            raise ValueError("Users must have an email address")
        if not date_of_birth:
            raise ValueError("Users must provide their date of birth")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        """Creates and returns a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, date_of_birth, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom User model extending Django's AbstractUser."""
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", "Can view records"),
            ("can_create", "Can create records"),
            ("can_edit", "Can edit records"),
            ("can_delete", "Can delete records"),
        ]

    objects = CustomUserManager()

    def __str__(self):
        return self.username