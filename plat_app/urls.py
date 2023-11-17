from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from plat_app import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostsViewSet)
router.register('register', views.UserCreateViewSet)
router.register('likes', views.LikesViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
]

urlpatterns += router.urls