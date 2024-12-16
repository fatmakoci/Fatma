from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100,null=True,blank=True )
    item_description =models.TextField(max_length=1000, null=True, blank=True )
    item_image = models.ImageField(upload_to="item/", null=True, blank=True)