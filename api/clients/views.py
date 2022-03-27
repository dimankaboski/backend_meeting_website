from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import permissions, generics, mixins, status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from utils.watermark import add_watermark
from utils.send_mail import send_mail
import logging

watermark_image = settings.WATERMARK
User = get_user_model()


class RegisterNewUser(CreateAPIView):

    model = User
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

class MatchAnotherUser(APIView):
    
    def get(self, request, pk):
        another_user = get_object_or_404(User, id=pk)
        user = request.user
        if another_user in user.liked.all():
            return Response({"message": f'Вы уже ставили лайк этому пользователю'}, status=status.HTTP_200_OK)
        else:
            user.liked.add(another_user)
            user.save()
        if user in another_user.liked.all() and another_user in user.liked.all():
            send_mail(user.email, another_user)
            send_mail(another_user.email, user)
            return Response({"message": f'{another_user.email}'}, status=status.HTTP_200_OK)   
        return Response({"message": f'Вы поставили лайк пользователю'}, status=status.HTTP_200_OK)