from rest_framework import serializers
from .models import UserModel, Likes, Posts
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    bio = serializers.CharField(max_length=350)
    birth_date = serializers.DateField()
    email = serializers.EmailField()

    class Meta:
        model = UserModel
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    liked_by = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=UserModel.objects.all())

    class Meta:
        model = Posts
        fields = ['created_at', 'body', 'liked_by', 'created_at']

    def update(self, instance, validated_data):
        liked_by = validated_data.pop('liked_by')
        for i in liked_by:
            instance.liked_by.add(i)
        instance.save()
        return instance


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ['posts_id', 'user_id']
