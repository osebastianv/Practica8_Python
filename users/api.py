from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from users.permissions import UserPermission
from users.serializers import UserListSerializer, UserDetailSerializer, NewUserSerializer


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

    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)

    #def perform_update(self, serializer):
    #    serializer.save(owner=self.request.user)
