from django.contrib import admin
from django.urls import path
from apps.posts.views import PostViewAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/posts/", PostViewAPI.as_view(),name='api_posts'),
]
