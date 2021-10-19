from django.db import models
from phone_field import PhoneField
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name= models.CharField(max_length=200)
    product_des = models.CharField(max_length=300)
    product_date = models.DateField()
    product_category = models.CharField(max_length=50,default="")
    product_subCategory = models.CharField(max_length=50, default="")
    product_price =  models.IntegerField(default=0)
    product_image = models.ImageField(upload_to= "shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name= models.CharField(max_length=100)
    contact_email = models.CharField(max_length=150)
    contact_phone = PhoneField(blank=True, help_text='Contact phone number')
    contact_subject = models.CharField(max_length=200)
    contact_desc = models.CharField(max_length=1000)



    def __str__(self):
        return self.contact_name
class orders(models.Model):
    order_id= models.AutoField(primary_key= True)
    items_json = models.CharField(max_length=2000, default='')
    name = models.CharField(max_length=200)
    email= models.CharField(max_length=150)
    phone = PhoneField(blank= True, help_text= 'Contact Phone Number')
    address= models.CharField(max_length=300)

class orderUpdate(models.Model):
    update_id= models.AutoField(primary_key= True)
    order_id = models.IntegerField(default="")
    desc = models.CharField(max_length=50000)
    timestamp= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.desc





