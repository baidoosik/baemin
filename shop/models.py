from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=100)                # 이름
    tel =  models.CharField(max_length=100)                 # 전화번호
    addr = models.CharField(max_length=100)                   # 주소

class Item(models.Model):
    shop = models.ForeignKey(Shop)                # 가게
    name = models.CharField(max_length=100)                 # 이름
    price = models.CharField(max_length=100)                # 가격

class Order(models.Model):
    shop = models.CharField(max_length=100)                 # 가게
    user = models.ForeignKey(settings.AUTH_USER_MODEL)                 # 주문한 유저
    item_set = models.ManyToManyField(Shop)             # 주문한 상품 목록 (Hint: ManyToManyField)
    created_at = models.DateTimeField(auto_now=True)           # 생성일시
# Create your models here.
