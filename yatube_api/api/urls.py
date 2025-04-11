from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import CommentViewSet, PostViewSet, GroupViewSet


v1_router = routers.SimpleRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/api-token-auth/", rest_framework_views.obtain_auth_token),
    path("v1/", include(v1_router.urls)),
]
