from django.contrib import admin

from .models import Apartment, Client, Review

admin.site.register(Apartment)
admin.site.register(Client)
admin.site.register(Review)
