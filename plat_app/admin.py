from django.contrib import admin
from .models import Posts, UserModel, Likes

# Register your models here.

admin.site.register([Posts, UserModel, Likes])