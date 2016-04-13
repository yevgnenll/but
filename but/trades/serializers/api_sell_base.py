from rest_framework import serializers

from trades.models import Sell


class SellBaseModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            source="user.username",
    )

    class Meta:

        model = Sell

        fields = (
                'pk',
                'title',
                'goods_name',
                'username',
                'sub_title',
                'stock',
                'sold_count',
                'price',
                'welcome_image',
        )
