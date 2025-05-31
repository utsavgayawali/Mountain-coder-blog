from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    content = HTMLField()
    short_desc = models.CharField(max_length=400, default="")
    slug =models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

def __str__(self):
     return self.title
    
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_image/')
    title = models.CharField(max_length=40)
    subtitle=models.CharField(max_length=50)
                                                                                                                                                
def __str__(self):
     return self.title

class Contact(models.Model):
    sn=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    description=models.TextField(max_length=40)

def __str__(self):
      return self.name






