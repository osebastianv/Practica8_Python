from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

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

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserPostListSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'url']
        extra_kwargs = {
            'url': {'view_name': 'user-post-list', 'lookup_field': 'username'},
        }
