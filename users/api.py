from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from users.permissions import UserPermission, UserPostPermission
from users.serializers import UserListSerializer, UserDetailSerializer, NewUserSerializer, UserPostListSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [UserPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['username', 'first_name', 'last_name']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewUserSerializer
        elif self.action == 'list':
            return UserListSerializer
        else:
            return UserDetailSerializer


class UserPostViewSet(ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [UserPostPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        return UserPostListSerializer
