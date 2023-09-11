from django.db import models

# Create your models here.
class userregister_db(models.Model):
    uname = models.CharField(max_length=100,null=True,blank=True)
    uemail = models.EmailField(max_length=50,null=True,blank=True)
    upass = models.CharField(max_length=30,null=True,blank=True)