from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Editorial(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_editorial = models.BooleanField(default=True)
    editorial_name = models.CharField(max_length=100, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'editorial_name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.editorial_name
    
    groups = models.ManyToManyField(Group, related_name='editorial_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='editorial_user_permissions')

class Reader(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_editorial = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username
    
    groups = models.ManyToManyField(Group, related_name='reader_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='lector_user_permissions')