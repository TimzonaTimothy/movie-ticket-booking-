from django.db import models
import datetime

# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="Vikas Sharma")
    address = models.CharField(max_length=150,default="IFCO Chowk, Delhi")
    phone = models.IntegerField(default='+91 8171415434')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Movie(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class buyer(models.Model):
    code = models.CharField(max_length=200, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    no_ticket = models.IntegerField(null=True)
    amount_paid = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False, null=True)
    purchase_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(buyer, on_delete=models.CASCADE, null=True)
    ref = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.ref

