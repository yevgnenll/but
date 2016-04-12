from rest_framework import serializers

from trades.models import Sell


class SellModelsSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            source="user.username",
    )

    class Meta:

        model = Sell

        fields = (
                'title',
                'goods_name',
                'username',
                'sub_title',
                'stock',
                'sold_count',
                'price',
                'welcome_image',
                'sub_image',
                'second_image',
                'goods_description',
                'is_public',
                'created_at',
                'updated_at',
                'hash_id',
        )
