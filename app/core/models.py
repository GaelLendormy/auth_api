from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                            PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Create and saves a new super user"""
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=False)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='', null=True)
    last_name = models.CharField(max_length=255, blank=True, default='', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
