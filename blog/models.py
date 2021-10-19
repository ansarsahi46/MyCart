from django.db import models

# Create your models here.
class blogPosts(models.Model):
    post_id = models.AutoField(primary_key= True)
    post_title= models.CharField(max_length=1000)
    head0= models.CharField(max_length=1000)
    chead0= models.CharField(max_length=10000)
    head1= models.CharField(max_length=1000)
    chead1= models.CharField(max_length=10000)
    head2= models.CharField(max_length=1000)
    chead2= models.CharField(max_length=10000)
    publish_date = models.DateField()
    post_image = models.ImageField(upload_to= "shop/images", default="")

