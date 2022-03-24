from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework import permissions, generics, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin

from .serializers import UserSerializer
from utils.watermark import add_watermark

import logging

watermark_image = settings.WATERMARK

class RegisterNewUser(CreateAPIView, CreateModelMixin):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        water_photo = add_watermark(user.photo, watermark_image, opacity=0.3)
        user.photo = water_photo
        user.save()
        return user