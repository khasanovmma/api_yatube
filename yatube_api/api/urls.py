from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import PostViewSet, GroupViewSet


router = routers.SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
urlpatterns = [
    path("api-token-auth/", rest_framework_views.obtain_auth_token),
    path("", include(router.urls)),
]
