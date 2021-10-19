import uuid
from django.db import models

# Create your models here.

class MOTD(models.Model):
    MessageOTD = models.TextField(max_length=260)
    def __str__(self):
        return self.Name


class Products(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)
    Pweight = models.DecimalField(max_digits=4, decimal_places=2)
    Pheight = models.DecimalField(max_digits=4, decimal_places=2)
    Saleprice = models.DecimalField(max_digits=5, decimal_places=2)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
   # Scene = models.TextChoices('Figure', 'Scene', null=True)
   # Media = models.TextChoices('Video Games', 'Memes', null=True )
    Thumbnail = models.ImageField(null=True, blank=True, upload_to='media') #https://www.youtube.com/watch?v=ygzGr51dbsY
    Stock = models.IntegerField(null=True, blank=False)
    SoldCount = models.IntegerField(null=True, blank=False)
    Active = models.BooleanField(default=True)
    UUID = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.Name


class Images(models.Model):
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)
    Image = models.ImageField(null=True, blank=True,
                                  upload_to='media')   # https://www.youtube.com/watch?v=ygzGr51dbsY

    def __str__(self):
        return self.Products.Name