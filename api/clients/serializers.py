from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            sex=validated_data['sex'],
            photo=validated_data['photo'],
            password=validated_data['password'],
            lat=validated_data['lat'],
            lon=validated_data['lon'],
        )
        return user

    class Meta:
        model = User
        fields = ( "id", "email", "password", "first_name", "last_name", "sex", "photo", "lat", "lon")


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "sex", "photo")