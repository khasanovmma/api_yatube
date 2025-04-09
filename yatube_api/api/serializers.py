from rest_framework import serializers
from posts.models import Group, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Post
        fields = ("id", "text", "pub_date", "image", "group", "author")

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentBaseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        required=False,
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False
    )

    class Meta:
        model = Comment
        fields = ("id", "text", "created", "post", "author")


class CommentSerializer(CommentBaseSerializer):
    post = serializers.SlugRelatedField(read_only=True, slug_field="text")
