from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userinfo(models.Model):
    username= models.CharField(max_length=100,unique=True)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.CharField(max_length=100)

class Posts(models.Model):
    username= models.ForeignKey(Userinfo, to_field='username', db_column='username',on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    content= models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon=models.DateTimeField(auto_now= True)
    status = models.IntegerField( default=0)
    img = models.ImageField(upload_to='pics')
    seen_no = models.IntegerField()

class Postsdata(models.Model):
    uname= models.ForeignKey(User,on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    content= models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon=models.DateTimeField(auto_now= True)
    status = models.IntegerField( default=0)
    img = models.ImageField(upload_to='pics')
    seen_no = models.IntegerField( default=0)
