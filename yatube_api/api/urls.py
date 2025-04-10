from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import CommentDetailView, PostViewSet, GroupViewSet


router = routers.SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
urlpatterns = [
    path("v1/api-token-auth/", rest_framework_views.obtain_auth_token),
    path(
        "v1/posts/<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view()
    ),
    path("v1/", include(router.urls)),
]
