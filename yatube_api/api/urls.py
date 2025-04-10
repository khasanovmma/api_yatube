from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import CommentDetailView, PostViewSet, GroupViewSet


v1_router = routers.SimpleRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="groups")
urlpatterns = [
    path("v1/api-token-auth/", rest_framework_views.obtain_auth_token),
    path("v1/", include(v1_router.urls)),
    path(
        "v1/posts/<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
    ),
]
