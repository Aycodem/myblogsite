from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length =100)
    body=models.CharField(max_length = 10000000)
    img=models.ImageField(upload_to = 'images/',default="default.jpg")
    created_at= models.DateTimeField(default=datetime.now,blank=True)