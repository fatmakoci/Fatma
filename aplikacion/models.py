from django.db import models

# Create your models here.
# Many-to-one/one-to-many

class Category(models.Model):
       category_name = models.CharField(max_length=100,null=True, blank=True )
       def __str__(self):
             return F"{self.category_name}"
class color(models.Model):
       color_name = models.CharField(max_length=100,null=True, blank=True )
       def __str__(self):
             return F"{self.color_name}"
# Many-to-many
class Item(models.Model):
    item_name = models.CharField(max_length=100,null=True,blank=True )
    item_description =models.TextField(max_length=1000, null=True, blank=True )
    item_image = models.ImageField(upload_to="item/", null=True, blank=True)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    item_colors = models.ManyToManyField(color,null=True, blank=True)

    def __str__(self):
           return f"{self.item_name}"

class Contact(models.Model):
       contact_name = models.CharField(max_length=100, null=True, blank=True )
       contact_surname = models.CharField(max_length=100, null=True, blank=True )
       contact_email = models.EmailField(null=True, blank=True )
       contact_comment = models.TextField(max_length=100, null=True, blank=True )

       def __str__(self):
           return f"{self.contact_name} {self.contact_surname}" 