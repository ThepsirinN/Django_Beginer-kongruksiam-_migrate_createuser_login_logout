from django.db import models

# Create your models here.
# model สำหรับการ makemigrationห และ migrate ฐานข้อมูล
class Post(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()