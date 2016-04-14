from rest_framework import serializers

from trades.serializers import CommentModelSerializer
from .api_sell_list import SellBaseModelSerializer


class SellDetailModelSerializer(SellBaseModelSerializer):

    comment = CommentModelSerializer(
            source="comment_set.all",
            many=True,
    )

    class Meta(SellBaseModelSerializer.Meta):

        fields = SellBaseModelSerializer.Meta.fields + (
                'sub_title',
                'stock',
                'sold_count',
                'sub_image',
                'second_image',
                'goods_description',
                'created_at',
                'updated_at',
                'hash_id',
                'comment',
        )
