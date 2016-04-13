from rest_framework.generics import ListAPIView

from trades.serializers import SellModelListSerializer
from trades.models import Sell


class SellListAPIView(ListAPIView):

    serializer_class = SellModelListSerializer
    queryset = Sell.objects.is_public_true()
