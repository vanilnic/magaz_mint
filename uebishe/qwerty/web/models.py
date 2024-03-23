from django.contrib.auth.models import AbstractUser
from django.db import models
from django_mysql.models.fields import SizedTextField

class Users(AbstractUser):
    ...
# Create your models here.
class Tea(models.Model):
    title = models.CharField('название чая', max_length=255)
    price = models.IntegerField('цена чая')
    count = models.IntegerField('количество чая')
    images = SizedTextField('изображение', size_class=3)

    def __str__(self):
        return self.title

class Balance(models.Model):
    user_id = models.IntegerField()
    money = models.IntegerField()

    def __str__(self):
        return str(self.money)

class Basket(models.Model):
    user_id = models.IntegerField()
    tea_id = models.IntegerField()
    count = models.IntegerField('скока шт')

    def __str__(self):
        return self.user_id