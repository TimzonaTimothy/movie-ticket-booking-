from django.contrib import admin
from . models import seller,buyer,Payment, Movie
# Register your models here.
admin.site.register(Movie)
# admin.site.register(seller)
admin.site.register(buyer)
# admin.site.register(Payment)
