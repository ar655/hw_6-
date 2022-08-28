from django.db import models

from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=10)
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client')
    address = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    bottles_ordered = models.IntegerField(default=0)
    photo = models.ImageField(
        verbose_name='photo',
        upload_to='photos',
        null=True,
        blank=True

    )



class Order(models.Model):
    client = models.ForeignKey(
        to=Client,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='order'

    )
    ordered_at = models.DateTimeField(
        verbose_name='дата и время заказа',
        auto_now_add = True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата и время изменения заказа',
        auto_now=True,
    )
    discription = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=10)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.contacts}"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'





