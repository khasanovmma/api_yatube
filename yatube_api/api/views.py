from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from posts.models import Group, Post, Comment
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["GET", "POST"])
    def comments(self, request, *args, **kwargs):
        post = self.get_object()
        if request.method == "GET":
            serializer = CommentSerializer(post.comments.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])

    def get_object(self):
        return self.get_queryset().filter(pk=self.kwargs["comment_id"]).first()

    def check_author_permission(self, obj):
        if obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if self.request.user != obj.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return None

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        permission_error = self.check_author_permission(obj)
        if permission_error:
            return permission_error
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        permission_error = self.check_author_permission(obj)
        if permission_error:
            return permission_error
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        permission_error = self.check_author_permission(obj)
        if permission_error:
            return permission_error
        return self.destroy(request, *args, **kwargs)
