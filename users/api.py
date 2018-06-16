from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from users.permissions import UserPermission, UserPostPermission
from users.serializers import UserListSerializer, UserDetailSerializer, NewUserSerializer, UserPostListSerializer

from rest_framework.response import Response
#from django.urls import reverse
from rest_framework.reverse import reverse

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

"""
    def list(self, request):
        year = 23
        data = {
            'year-summary-url': reverse('year-summary', args=[year], request=request)
        }
        return Response(data)

    def get_url(self, obj, view_name, request):
        kwargs = {'username': obj.get('username')}
        return reverse(view_name, kwargs=kwargs, request=request)
"""