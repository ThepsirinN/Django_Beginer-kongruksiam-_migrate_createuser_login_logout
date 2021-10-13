from django.contrib import admin
# import model post จาก ไฟล์ mode;
from .models import Post
# Register your models here.

admin.site.register(Post)