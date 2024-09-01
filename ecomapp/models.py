from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class contactenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    message = models.TextField()


class Menu(models.Model):
    CAT = ((1, 'Maharashtrian Dishes'), (2, 'SouthIndian Dishes'), (3, 'Gujarati Dishes'), (4, 'Chinese Dishes'),
           (5, 'Sweets'),
           (6, 'Non-veg Foods'))
    name = models.CharField(max_length=50, verbose_name='Menu Name')
    price = models.FloatField()
    cat = models.IntegerField(verbose_name='Categorynsi', choices=CAT)
    pdetail = models.CharField(max_length=300, verbose_name='Menu Details')
    is_active = models.BooleanField(default=True)
    pimage = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Cart(models.Model):
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey('Menu', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)


class Order(models.Model):
    orderid = models.IntegerField()
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey('Menu', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)
    amt = models.FloatField()



class Orderhistory(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
