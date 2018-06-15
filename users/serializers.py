from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

class UserListSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username']


class NewUserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
