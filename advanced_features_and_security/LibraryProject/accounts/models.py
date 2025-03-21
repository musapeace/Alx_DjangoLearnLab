from django.db import models
from django.db import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('users must have an email address')
        if not date_of_birth:
            raise ValueError('users must provide their date of birth')
        

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, date_of_birth, password, **extra_fields)
    

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

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
        
