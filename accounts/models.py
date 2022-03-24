from django.db import models
from django.contrib.auth.models import AbstractUser


AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('username').blank = True
AbstractUser._meta.get_field('username')._unique = False

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class SEX:
        M = 'М'
        F = 'Ж'

        LIST_DISPLAY = (
            (M, 'Мужской'),
            (F, 'Женский')
        )
    
    sex = models.CharField('Пол', max_length=1, choices=SEX.LIST_DISPLAY, blank=True)
    photo = models.ImageField(upload_to='profiles', blank=True, verbose_name='Фото', default='default_user.png')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    