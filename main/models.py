from django.db import models


class Apartment(models.Model):
    address = models.CharField('address', max_length=100)
    area = models.FloatField('area')
    floorNumber = models.IntegerField('floorNumber')
    roomCount = models.IntegerField('roomCount')
    price = models.FloatField('price')
    picture = models.CharField('picture', max_length=100)

    class Meta:
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'


class Client(models.Model):
    firstName = models.CharField('firstName', max_length=30)
    lastName = models.CharField('lastName', max_length=30)
    email = models.EmailField(max_length=50, )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    apartment = models.ForeignKey(Apartment, on_delete=models.DO_NOTHING)
    content = models.TextField('context')
    datetime = models.DateTimeField('date')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
