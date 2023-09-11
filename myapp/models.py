from django.db import models

# Create your models here.
class counselor_db(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)


class blog_db(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="blogimg", null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)


