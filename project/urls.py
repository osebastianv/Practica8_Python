"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import HomeView, PostDetailView, NewPostView
from users.views import UsersView, UserPostView, LoginView, LogoutView, SignupView
from users.api import UserViewSet, UserPostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')
router.register('users', UserViewSet, base_name='users')
router.register('blogs', UserPostViewSet, base_name='blogs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('blogs/<username>/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('blogs/', UsersView.as_view(), name="user-list"),
    path('blogs/<username>', UserPostView.as_view(), name="user-post-list"),
    path('new-post', NewPostView.as_view(), name='new-post'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),

    # API URLs
    path('api/v1/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
