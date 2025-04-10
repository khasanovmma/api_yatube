from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import CommentViewSet, PostViewSet, GroupViewSet


v1_router = routers.SimpleRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_comment_urls = [
    path(
        "v1/posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comment-list",
    ),
    path(
        "v1/posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="comment-detail",
    ),
]
urlpatterns = [
    path("v1/api-token-auth/", rest_framework_views.obtain_auth_token),
    path("v1/", include(v1_router.urls)),
    *v1_comment_urls,
]
