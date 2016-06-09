from django.contrib import admin

from trades.models import Sell


@admin.register(Sell)
class SellAdminModel(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'user',
        'title',
        'sub_title',
        'price',
        'goods_name',
        'is_public',
    )

    search_fields = [
        'user',
        'title',
        'sub_title',
        'price',
        'goods_name',
        'is_public',
    ]

    list_filter = (
        'is_public',
    )
