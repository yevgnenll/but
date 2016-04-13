from rest_framework.generics import RetrieveAPIView

from trades.serializers import SellDetailModelSerializer
from trades.models import Sell


class SellDetailAPIView(RetrieveAPIView):

    serializer_class = SellDetailModelSerializer
    queryset = Sell.objects.all()
