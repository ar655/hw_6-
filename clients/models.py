from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    bottles_ordered = models.IntegerField(default=0)
    photo = models.ImageField(
        verbose_name='photo',
        upload_to='photos',
        null=True,
        blank=True

    )








