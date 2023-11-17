from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=350, null=True, blank=True)
    birth_date = models.DateField()
    email = models.EmailField()
    #liked_posts = models.ManyToManyField('Posts', through='Likes', related_name='liked_posts')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Posts(models.Model):
    user = models.ForeignKey(UserModel, related_name='posts', on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    liked_by = models.ManyToManyField(UserModel, through='Likes', through_fields=('posts', 'user'), related_name='liked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Likes(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like from {self.user} to {self.posts}'
