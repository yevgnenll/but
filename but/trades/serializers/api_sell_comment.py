from rest_framework import serializers

from trades.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            source="user.username",
    )
    profile_image = serializers.SerializerMethodField(
            'get_user_profile_image'
    )

    class Meta:

        model = Comment

        fields = (
                'content',
                'username',
                'created_at',
                'is_public',
                'profile_image',
        )

    def get_user_profile_image(self, comment):

        is_image = comment.user.profile_image
        if is_image:
            return is_image.url
        else:
            return None

    def create(self, kwargs):
        print(self,kwargs, 'ddddddddd')

        return Comment(**kwargs)
