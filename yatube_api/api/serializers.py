from rest_framework import serializers
from posts.models import Post


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
