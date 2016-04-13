from rest_framework import serializers

from trades.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            source="user.username",
    )

    class Meta:

        model = Comment

        fields = (
                'content',
                'username',
                'created_at',
                'is_public',
        )
