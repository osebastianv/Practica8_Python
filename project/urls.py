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
from django.urls import path

from posts.views import HomeView, PostDetailView
from users.views import UsersView, UserPostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('blogs/<username>/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('blogs/', UsersView.as_view(), name="user-list"),
    path('blogs/<username>', UserPostView.as_view(), name="user-post-list"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
