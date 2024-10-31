from django.urls import path
from apps.blog.views import PostListView


urlpatterns = [
    path("", PostListView.as_view(), name="home"),
]