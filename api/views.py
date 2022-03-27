from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import get_object_or_404

import django_filters.rest_framework as rest_filters
from rest_framework import permissions, generics, mixins, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from api.clients.serializers import UserListSerializer
from utils.geo import coord_range

import logging

watermark_image = settings.WATERMARK
User = get_user_model()


class UserPagination(PageNumberPagination):
    """Кол-во юзеров для пагинации"""
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class UserFilter(rest_filters.FilterSet):
    """Фильтр по юзерам"""
    first_name = rest_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = rest_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    distance = rest_filters.NumberFilter(method='filter_distance')

    def filter_distance(self, queryset, name, value):
        user = self.request.user
        coords_range = coord_range([user.lat, user.lon], dist=int(value))
        return queryset.filter(lat__range=[coords_range[0], coords_range[1]], lon__range=[coords_range[2], coords_range[3]])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'sex']


class UsersListView(ListAPIView):
    """Список всех пользователей"""
    permission_classes = [
        permissions.AllowAny
    ]
    model = User
    serializer_class = UserListSerializer
    pagination_class = UserPagination
    queryset = User.objects.all()
    filter_backends = [rest_filters.DjangoFilterBackend]
    filterset_class = UserFilter