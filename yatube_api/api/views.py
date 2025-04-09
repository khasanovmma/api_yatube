from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from api.permissions import IsAuthorOrReadOnly
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
