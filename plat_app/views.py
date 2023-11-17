from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response

from .models import UserModel, Posts, Likes
from .serializers import UserModelSerializer, PostsSerializer, LikesSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.decorators import action, api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        serializer = PostsSerializer(user.posts.all(), many=True)
        return Response(serializer.data)


class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.AllowAny]


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    #permission_classes = [permissions.IsAuthenticated]


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    #permission_classes = [permissions.IsAuthenticated]



