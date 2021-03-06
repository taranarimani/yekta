from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager


class User(AbstractUser):

    email = models.EmailField(verbose_name='Email addres',
                              max_length=250,
                              unique=True)
    username = models.CharField(verbose_name='Username',
                                max_length=50,
                                unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("users")
        ordering = ["-create_time", 'username']

    def get_email_field_name(self):
        return self.email

    def get_username(self):
        return self.username

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.admin

    def __str__(self):
        return self.email
