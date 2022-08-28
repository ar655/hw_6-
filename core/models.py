from django.db import models


from clients.models import Order

class Botlle(models.Model):

    volume = models.IntegerField(default=10)
    text = models.TextField(null=True,blank=True)
    expired = models.BooleanField(default=False)
    orders = models.ManyToManyField(
        to=Order,
        null =True,
        blank=True,
        verbose_name='заказы',
        related_name='bottles'

    )


class BottlesCount(models.Model):
    bottle = models.ForeignKey(
        to=Botlle,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bottlescount'

    )

    count = models.IntegerField(default=0)

    order = models.ForeignKey(
        to=Order,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bottlescount'

    )